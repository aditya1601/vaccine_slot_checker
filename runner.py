import requests
import datetime
import config
from utils import logger, play_sound
import time

headers_dict = {
    'dnt': '1',
    'origin': 'https://www.cowin.gov.in',
    'referer': 'https://www.cowin.gov.in/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
}

def get_json(loc_id):
    date = datetime.datetime.today().strftime("%d/%m/%Y")
    if config.SEARCH_BY == "district":
        url = config.URL_TEMPLATE_DISTRICT.format(loc_id, date)
    elif config.SEARCH_BY == "pincode":
        url = config.URL_TEMPLATE_PIN.format(loc_id, date)
    
    resp = requests.get(url, headers = headers_dict)
    if resp.status_code == 200:
        return resp.json()
    else:
        logger.error("### URL FAILED!! ###")
        logger.error(resp.status_code)
        logger.info("Waiting for 5 minutes now...")
        time.sleep(5*60)
        return None


def get_data():
    if config.SEARCH_BY == "pincode":
        all_json = [get_json(pin) for pin in config.PINCODES]
    elif config.SEARCH_BY == "district":
        all_json = [get_json(config.DISTRICT_ID)]
    
    centers = []
    num_young = 0
    num_adult = 0

    for data in all_json:
        if data and "centers" in data.keys():
            for center in data["centers"]:
                if "sessions" in center.keys():
                    for session in center["sessions"]:
                        if session["available_capacity"] != 0:
                            if session["min_age_limit"] == 18:
                                if config.DOSE == 1:
                                    if session["available_capacity_dose1"] != 0:
                                        centers.append(center)
                                elif config.DOSE == 2:
                                    if session["available_capacity_dose2"] != 0:
                                        centers.append(center)
                                num_young += 1
                            else:
                                num_adult += 1

    logger.debug(f"Available in {num_adult + num_young} centers : {num_young} (18+) and {num_adult} (45+)")

    return centers


def fetch_center_details():
    centers = get_data()

    if centers:
        for center in centers:
            for session in center["sessions"]:
                logger.info(
                    "Found {} slots ({}) in {} - (Pin : {}) on {}".format(
                        session["available_capacity"],
                        session["vaccine"],
                        center["name"],
                        center["pincode"],
                        session["date"]
                    )
                )
    else:
        logger.info("No 18+ slots found.")
        return False

    return True


if __name__ == "__main__":
    logger.info(f"Starting search for Dose {config.DOSE} slots...")
    if config.SEARCH_BY == "pincode":
        logger.info(f"PINCODES = {str(config.PINCODES)}")
    else:
        logger.info(f"DISTRICT_ID = {str(config.DISTRICT_ID)}")
    logger.info(f"Checking frequency : {config.SLEEP_INTERVAL} seconds")
    
    if config.SLEEP_INTERVAL > 0:
        while True:
            if fetch_center_details():
                play_sound()
            time.sleep(config.SLEEP_INTERVAL)
