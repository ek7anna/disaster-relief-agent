#import streamlit as st
#from agent import run_agent  # This calls the "brain" function (initially a placeholder)

# st.title("Disaster-Relief Resource Routing Agent")

# A static list of alerts you show on the UI (later this can come from a database)
# alerts = [
#     {"id": 1, "alert_text": "Flood in Ward 12, water level rising"},
#     {"id": 2, "alert_text": "Bridge collapse near NH 47, many trapped"},
#     {"id": 3, "alert_text": "Heavy rains causing landslide risk in Hillside area"},
# ]

# # Show alerts
# for alert in alerts:
#     st.write(f"**Alert {alert['id']}**: {alert['alert_text']}")
#     if st.button(f"Generate Plan for Alert {alert['id']}", key=alert['id']):
#         # When button clicked, call run_agent to get the plan and resources
#         output = run_agent(alert['id'])
#         st.subheader("Dispatch Plan")
#         st.write(output["dispatch_plan"])  # Show the text plan
#         st.write("Resources allocated:")
#         for resource in output['resources']:
#             st.write(f"- {resource['name']} ({resource['type']}) - Capacity: {resource.get('capacity', 'N/A')}")
import streamlit as st
import pandas as pd
from agent import run_agent

st.title("Disaster-Relief Resource Routing Agent")

alerts = [
    {"id": 1, "alert_text": "Flood in Ward 12, water level rising"},
    {"id": 2, "alert_text": "Bridge collapse near NH 47, many trapped"},
    {"id": 3, "alert_text": "Heavy rains causing landslide risk in Hillside area"},
]

alerts_df = pd.DataFrame(alerts)
st.subheader("Current Alerts")
st.dataframe(alerts_df)

for alert in alerts:
    st.write("")  # spacing
    st.markdown(f"### Alert {alert['id']}: {alert['alert_text']}")
    if st.button(f"Generate Plan for Alert {alert['id']}", key=alert['id']):
        with st.spinner('Generating dispatch plan...'):
            output = run_agent(alert['id'])
        st.subheader("Dispatch Plan")
        st.write(output["dispatch_plan"])
        with st.expander("Resources allocated (click to expand)"):
            resource_df = pd.DataFrame(output['resources'])
            st.dataframe(resource_df)
