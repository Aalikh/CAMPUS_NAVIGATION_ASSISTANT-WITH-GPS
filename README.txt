LIVE GPS ADD-ON FOR STREAMLIT
=============================

WHAT THIS ADD-ON DOES
- Adds Start live GPS and Stop controls.
- Uses the browser's Geolocation API watchPosition(), so the location is
  updated as the device moves while tracking is running.
- Sends location updates to the Streamlit Python app approximately every
  1.5 seconds.
- Includes a small demo app that displays the latest coordinates on a map.

IMPORTANT
- The user must explicitly press Start and grant browser location permission.
- Use the deployed HTTPS URL (Streamlit Community Cloud uses HTTPS).
- GPS accuracy depends on the device, browser, signal and permissions.
- This is foreground tracking: keep the page open. It does not track after
  the user stops it, closes the page, or the browser suspends it.
- Do not collect or store people's location without clear notice and consent.
- This ZIP is an add-on module, not a replacement for your existing app.

HOW TO ADD IT TO YOUR EXISTING PROJECT
1. Extract this ZIP into your project folder.
2. Keep gps_tracker.py and the gps_component folder in the same folder as
   your main Streamlit Python file (for example app.py).
3. Add the packages from requirements.txt to your project's requirements.txt.
   If you already have a requirements.txt, add the missing lines rather than
   replacing your existing dependencies.
4. In your main Python file, add:
       import pandas as pd
       from gps_tracker import gps_tracker
5. Where you want the GPS controls to appear, add:

       location = gps_tracker()

       if isinstance(location, dict) and location.get("latitude") is not None:
           lat = location["latitude"]
           lon = location["longitude"]
           st.write(f"Latitude: {lat:.6f}")
           st.write(f"Longitude: {lon:.6f}")
           st.map(
               pd.DataFrame({"lat": [lat], "lon": [lon]}),
               latitude="lat",
               longitude="lon",
               zoom=17
           )

6. Commit the files to the same GitHub repository connected to Streamlit
   Community Cloud. Streamlit will install requirements and redeploy.

DEMO / LOCAL TEST
- Install: pip install -r requirements.txt
- Run: streamlit run example_app.py

TO FINISH THE INTEGRATION
Your live website could not be inspected by the browser tool (it redirected
to a Streamlit access/authentication page). To merge this into your exact
Campus Navigation app and place the moving marker on its existing campus map,
provide your GitHub repository URL or upload the project's ZIP/source files.
Do not share passwords, API keys, or private tokens.
