import streamlit as st
import pandas as pd
from gps_tracker import gps_tracker

st.set_page_config(page_title="Live GPS Demo", page_icon="📍")
st.title("📍 Live GPS Tracker")
st.caption("Your location is requested only after you press Start live GPS.")

location = gps_tracker()

if isinstance(location, dict) and location.get("latitude") is not None:
    lat = location["latitude"]
    lon = location["longitude"]
    accuracy = location.get("accuracy")
    st.success("Live location received")
    st.metric("Latitude", f"{lat:.6f}")
    st.metric("Longitude", f"{lon:.6f}")
    if accuracy is not None:
        st.caption(f"Reported GPS accuracy: ±{accuracy:.0f} metres")
    st.map(pd.DataFrame({"lat": [lat], "lon": [lon]}), latitude="lat", longitude="lon", zoom=17)
elif isinstance(location, dict) and location.get("tracking") is False:
    st.info("GPS tracking is stopped.")
else:
    st.info("Press **Start live GPS** below and allow location permission.")
