# Vaccine Slot Checker for Cowin

This is a script made for personal use to check covid vaccine slots on cowin. I usually start this script and keep it running in a terminal whole day. To keep it very simple I have intentionally not included any UI or background process.

### DISCLAIMER :
```This script is using Cowin public APIs. The appointment availability data is cached and may be upto 30 minutes old. Further, these APIs are subject to a rate limit of 100 API calls per 5 minutes per IP. [Updated on 11 May 2021]```

## Setup
* Install Python (>=3.6)
* Edit `config.py` with your pincode details

Before running for the first time, install some dependencies using the following command

```pip install -r requirements.txt```
  
## Run script
```python runner.py```

Press Ctrl+C or close the terminal to stop the script.

The script will notify you by playing a sound when an 18+ vaccination slot is available. You can easily modify the script runner.py for getting 45+ slot notifications as well.