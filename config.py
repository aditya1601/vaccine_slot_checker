LOGGING_LEVEL = "INFO"

NUM_TIMES_NOTIFY = 3            # Number of times the notification tone is played if a slot is found
RUN_EVERY = 10                  # Run the search every (x) minutes

# To search using pin code
URL_TEMPLATE = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}"
LOCATION_IDENTIFIER = 474002    # Enter Pin code here

# To search using district
# URL_TEMPLATE = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}"
# LOCATION_IDENTIFIER = 313       # District id, can be found using inspect element in browser


