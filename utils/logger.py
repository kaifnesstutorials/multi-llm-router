import json
from datetime import datetime

LOG_FILE = "logs/usage.json"

def log_usage(entry):

    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append({
        "timestamp": str(datetime.now()),
        **entry
    })

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)
