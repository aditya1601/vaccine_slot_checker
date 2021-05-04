import requests
import datetime
import config
from utils import logger, play_sound
import time


def get_json(loc_id, date):
    url = config.URL_TEMPLATE.format(loc_id, date)
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    else:
        logger.error("######## URL FAILED!! #########")
        return None


def get_dates():
    dates = []
    today = datetime.datetime.now()
    dates.append(today.strftime("%d-%m-%Y"))
    for i in range(5):
        today = today + datetime.timedelta(7)
        dates.append(today.strftime("%d-%m-%Y"))
    logger.debug(f"# Dates : {dates} #")
    return dates


def get_data():
    all_json = [get_json(config.LOCATION_IDENTIFIER, date) for date in get_dates()]

    centers = []
    num_young = 0
    num_adult = 0

    for data in all_json:
        if data and "centers" in data.keys():
            for center in data["centers"]:
                if "sessions" in center:
                    for session in center["sessions"]:
                        if session["available_capacity"] != 0:
                            if session["min_age_limit"] == 18:
                                num_young += 1
                                centers.append(center)
                            else:
                                num_adult += 1

    logger.debug(f"Available in {num_adult + num_young} centers : {num_young} (18+) and {num_adult} (45+)")

    return centers


def fetch_center_details():
    centers = get_data()
    total_slots = 0

    if centers:
        for center in centers:
            for session in center["sessions"]:
                slots = session["available_capacity"]
                total_slots += slots
                fee = center["fee_type"]
                name = center["name"]
                date = session["date"]
                logger.info(f"############[{fee}] {slots} slots on {date} in {name}")
    else:
        logger.info("No 18+ slots found.")

    return total_slots


if __name__ == "__main__":
    if config.RUN_EVERY > 0:
        while True:
            available_slots = fetch_center_details()
            if available_slots > 0:
                play_sound()
            time.sleep(config.RUN_EVERY * 60)
