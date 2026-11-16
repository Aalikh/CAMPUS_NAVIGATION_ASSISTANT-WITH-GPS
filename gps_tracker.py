from pathlib import Path
import streamlit.components.v1 as components

_COMPONENT_DIR = Path(__file__).parent / "gps_component"

_gps_component = components.declare_component(
    "live_gps_tracker",
    path=str(_COMPONENT_DIR),
)

def gps_tracker(key: str = "live_gps"):
    """Return the latest browser GPS reading while the user has tracking enabled.

    Returns a dict with latitude, longitude, accuracy, speed, heading,
    timestamp and tracking. Returns None before the first GPS update.
    """
    return _gps_component(key=key, default=None)
