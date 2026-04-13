import json
from datetime import datetime

def log_alert(prediction):
    alert = {
        "timestamp": str(datetime.now()),
        "prediction": prediction
    }

    try:
        with open("outputs/alerts.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(alert)

    with open("outputs/alerts.json", "w") as f:
        json.dump(data, f, indent=4)