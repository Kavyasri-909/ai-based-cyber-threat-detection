import streamlit as st

st.title("Cyber Threat Detection Dashboard")

st.write("Recent Alerts:")

try:
    with open("../outputs/alerts.json", "r") as f:
        for line in f:
            st.write(line)
except:
    st.write("No alerts yet")