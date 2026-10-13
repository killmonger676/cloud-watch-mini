import random
from datetime import datetime
import streamlit as st
import pandas as pd

st.set_page_config(page_title="CloudWatch Mini", page_icon="☁️", layout="wide")

st.markdown("""
<style>
.main {background-color: #0b1220;}
.block-container {padding-top: 2rem;}
div[data-testid="stMetric"] {background: #111c2f; padding: 16px; border-radius: 12px; border: 1px solid #26364f;}
</style>
""", unsafe_allow_html=True)

st.title("☁️ CloudWatch Mini")
st.caption("A local learning prototype inspired by cloud server monitoring — simulated data, not connected to AWS.")

with st.sidebar:
    st.header("Simulation controls")
    cpu_threshold = st.slider("CPU alarm threshold (%)", 50, 95, 80, 5)
    force_alert = st.toggle("Simulate a high-CPU incident", value=True)
    st.divider()
    st.caption("Demo mode: metrics are fictional and generated locally.")

servers = [
    {"Server": "web-server-01", "CPU (%)": random.randint(18, 55), "Memory (%)": random.randint(35, 68), "Region": "ap-south-1"},
    {"Server": "api-server-02", "CPU (%)": random.randint(25, 65), "Memory (%)": random.randint(40, 76), "Region": "ap-south-1"},
    {"Server": "worker-server-03", "CPU (%)": random.randint(20, 60), "Memory (%)": random.randint(30, 70), "Region": "ap-south-1"},
]
if force_alert:
    servers[1]["CPU (%)"] = random.randint(max(cpu_threshold + 1, 82), 98)

df = pd.DataFrame(servers)
df["Status"] = df["CPU (%)"].apply(lambda cpu: "ALARM" if cpu >= cpu_threshold else "HEALTHY")
alarm_count = int((df["Status"] == "ALARM").sum())
avg_cpu = round(df["CPU (%)"].mean(), 1)
avg_mem = round(df["Memory (%)"].mean(), 1)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Servers monitored", len(df))
m2.metric("Average CPU", f"{avg_cpu}%")
m3.metric("Average memory", f"{avg_mem}%")
m4.metric("Active alarms", alarm_count, delta="Needs attention" if alarm_count else "All clear", delta_color="inverse")

st.subheader("Server health")
def color_status(val):
    if val == "ALARM":
        return "background-color: #5b202b; color: #ffd6dc; font-weight: bold"
    return "background-color: #153d34; color: #c8ffeb; font-weight: bold"

st.dataframe(df.style.map(color_status, subset=["Status"]), use_container_width=True, hide_index=True)

st.subheader("Resource utilization")
chart_df = df.set_index("Server")[["CPU (%)", "Memory (%)"]]
st.bar_chart(chart_df, y=["CPU (%)", "Memory (%)"], use_container_width=True)

st.subheader("Automated recommendations")
for _, row in df.iterrows():
    if row["Status"] == "ALARM":
        st.error(f"🚨 {row['Server']} is at {row['CPU (%)']}% CPU, above the {cpu_threshold}% threshold. Check recent traffic, running processes, and application logs; scale resources if the load is sustained.")
    elif row["Memory (%)"] >= 70:
        st.warning(f"⚠️ {row['Server']} memory usage is {row['Memory (%)']}%. Review memory-heavy processes.")
    else:
        st.success(f"✅ {row['Server']} is within the configured CPU threshold.")

st.caption(f"Last refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} · Refresh the page to generate a new sample.")
with st.expander("What AWS services does this demonstrate?"):
    st.markdown("""
    - **Amazon EC2:** the virtual servers being represented.
    - **Amazon CloudWatch:** the real AWS service that collects metrics and supports alarms.
    - **Amazon SNS:** could be added to send notifications when an alarm fires.

    This prototype does not call AWS APIs, does not read real server metrics, and does not send notifications.
    """)
