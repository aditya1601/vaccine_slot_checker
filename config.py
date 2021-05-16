# Provide a list of pincodes to search on (can contain a single pincode also)
# For example : PINCODES = [474002]
PINCODES = [474002, 474001]

# Select the dose you want to search the slots for. Valid options are 1 or 2
DOSE = 1



# Change below configuration only when you know what you are doing
# ================================================================

# Please select how you want to search the slot
# Valid option are : "pincode" or "district"
SEARCH_BY = "pincode"

# Provide a district_id, if SEARCH_BY = "district"
# Check the request URL from the browser's network tab in developer tools
DISTRICT_ID = 313

# Don't change below details
# ==========================
URL_TEMPLATE_PIN = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}"
URL_TEMPLATE_DISTRICT = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}"
LOGGING_LEVEL = "INFO"

# Setting sleep interval automatically based on the rate limit of 100 requests/5 minutes
MIN_SLEEP_INTERVAL = 10
SLEEP_INTERVAL = 10

if SEARCH_BY == "pincode":
    SLEEP_INTERVAL = 5*len(PINCODES)
if MIN_SLEEP_INTERVAL>SLEEP_INTERVAL:
    SLEEP_INTERVAL = MIN_SLEEP_INTERVAL
