from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="PAWSENSE-X",
    page_icon="    ",
    layout="wide"
)

st.title("     PAWSENSE-X")
st.caption("AI Animal Welfare & Danger Intelligence")

st.success("     SYSTEM ONLINE  |  DEMO / TEST MODE")

st.divider()

# KPI cards
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Animal Detected", "DOG")

with c2:
    st.metric("Confidence", "89.69%")

with c3:
    st.metric("Risk Score", "87 / 100", "+87")

with c4:
    st.metric("Risk Level", "CRITICAL")

st.divider()

# Main intelligence
left, right = st.columns(2)

with left:
    st.subheader("     Animal Intelligence")

    image_path = Path(r"data/dog.png")
    if image_path.exists():
        st.image(str(image_path), caption="Detected Animal - Dog", width="stretch")

    st.write("**Species:** Dog")
    st.write("**Tracking ID:** Animal #1")
    st.write("**Status:** ACTIVE")
    st.write("**Detection Confidence:** 89.69%")

    st.progress(0.8969)

    st.write("**Behavior Status:**")
    st.warning("ABNORMAL MOVEMENT")

    st.write("**Movement Distance:** 195.06 pixels")

with right:
    st.subheader("       Environmental Risk")

    st.write("**Zone Status:**")
    st.error("CRITICAL ZONE")

    st.write("**Animal Position:** (520, 280)")
    st.write("**Road Proximity:** +30")
    st.write("**Vehicle Proximity:** +25")

    st.write("**Risk Components**")

    st.progress(0.30)
    st.caption("Road proximity     30 points")

    st.progress(0.25)
    st.caption("Vehicle proximity     25 points")

st.divider()

# Risk explanation
st.subheader("     Explainable Risk Alert")

st.error("Potential animal welfare risk detected")

st.write("The risk engine identified the following contributing factors:")

f1, f2 = st.columns(2)

with f1:
    st.write("     Near danger zone")
    st.write("     Vehicle proximity detected")

with f2:
    st.write("     Abnormal movement pattern")
    st.write("     Behavior differs from baseline")

st.divider()

# Timeline
st.subheader("     Event Timeline")

events = [
    ("DETECTION", "Dog detected with 89.69% confidence", "INFO"),
    ("BEHAVIOR", "Abnormal movement pattern detected", "WARNING"),
    ("DANGER ZONE", "Animal entered critical zone", "CRITICAL"),
    ("RISK", "Welfare risk score reached 87/100", "CRITICAL")
]

for event_type, message, severity in events:
    st.write(f"**{event_type}**  |  {message}  |  `{severity}`")

st.divider()

st.info(
    "Human verification recommended. "
    "PAWSENSE-X identifies potential welfare risks; "
    "it does not diagnose medical conditions or emotions."
)

st.caption(
    "PAWSENSE-X | Explainable AI for Animal Welfare Monitoring"
)

