import json
from datetime import datetime

def send_alert(status):
    alert = {
        "time": str(datetime.now()),
        "status": status
    }

    with open("outputs/alerts.json", "a") as f:
        json.dump(alert, f)
        f.write("\n")