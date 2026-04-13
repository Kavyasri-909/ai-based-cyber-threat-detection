import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Cyber Threat Detection Dashboard", layout="wide")

st.title("🛡️ Cyber Threat Detection Dashboard")

# Simulated alerts (you can later replace with real ML/API data)
threat_types = [
    "Malware Detected",
    "Suspicious Login Attempt",
    "DDoS Activity",
    "Phishing Attempt",
    "Unauthorized Access"
]

severities = ["Low", "Medium", "High", "Critical"]

# Generate sample alerts
def generate_alerts(n=5):
    alerts = []
    for _ in range(n):
        alerts.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": random.choice(threat_types),
            "severity": random.choice(severities)
        })
    return alerts

st.subheader("🚨 Recent Alerts")

if "alerts" not in st.session_state:
    st.session_state.alerts = generate_alerts()

if st.button("🔄 Refresh Alerts"):
    st.session_state.alerts = generate_alerts()

alerts = st.session_state.alerts

if alerts:
    for alert in alerts:
        if alert["severity"] == "Critical":
            st.error(f"{alert['time']} - {alert['type']} ({alert['severity']})")
        elif alert["severity"] == "High":
            st.warning(f"{alert['time']} - {alert['type']} ({alert['severity']})")
        else:
            st.info(f"{alert['time']} - {alert['type']} ({alert['severity']})")
else:
    st.success("No alerts detected")