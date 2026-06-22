import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh
import time
import os

st.set_page_config(
    page_title="Smart Home AI Control Center",
    layout="wide"
)

st_autorefresh(interval=1000,key="refresh")

if "logged_in" not in st.session_state:
    st.session_state.logged_in=False

if not st.session_state.logged_in:

    st.title("🏠 Smart Home Secure Login")

    user=st.text_input("Username")
    password=st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if user=="admin" and password=="1234":

            st.session_state.logged_in=True
            st.rerun()

        else:
            st.error("Invalid Login")

    st.stop()

file="simulation/status.csv"

if not os.path.exists(file):

    st.error("No simulation data")
    st.stop()

df=pd.read_csv(file)

latest=df.iloc[-1]

light=int(latest["Light"])
fan=int(latest["Fan"])
ac=int(latest["AC"])
alarm=int(latest["Alarm"])
energy=int(latest["Energy"])

st.title("🏠 Real-Time Smart Home AI Center")

c1,c2,c3,c4,c5=st.columns(5)

c1.metric("💡 Light","ON" if light else "OFF")
c2.metric("🌀 Fan","ON" if fan else "OFF")
c3.metric("❄ AC","ON" if ac else "OFF")
c4.metric("🚨 Alarm","ACTIVE" if alarm else "SAFE")
c5.metric("⚡ Energy","SAVE" if energy else "NORMAL")

st.divider()

st.subheader("🎤 Voice Command Simulation")

v1,v2,v3=st.columns(3)

with v1:
    st.button("Turn Light ON")

with v2:
    st.button("Turn Fan ON")

with v3:
    st.button("Activate Alarm")

left,right=st.columns([2,1])

with left:

    st.subheader("🏠 Home Map")

    st.code("""
┌──────────────────────┐
│ Bedroom 💡          │
│                      │
│ Living Room 🛋🌀     │
│                      │
│ Kitchen 🍳          │
│                      │
│ Door 🚪             │
└──────────────────────┘
""")

with right:

    st.subheader("🌀 Fan Animation")

    if fan:

        spin=st.empty()

        chars=["|","/","-","\\"]

        for i in range(4):

            spin.write(
                f"Fan Running {chars[i]}"
            )

            time.sleep(.1)

    else:
        st.write("Fan OFF")

st.divider()

df["Power"]=(
df["Light"]*20
+df["Fan"]*60
+df["AC"]*120
)

st.subheader("⚡ Real-Time Power Usage")

st.line_chart(df["Power"])

avg=df["Power"].mean()

st.metric(
"Average Power",
f"{round(avg,2)}W"
)

st.divider()

st.subheader("🤖 Smart Assistant")

q=st.text_input("Ask assistant")

if q:

    q=q.lower()

    if "energy" in q:
        st.info("Current power usage normal")

    elif "alarm" in q:
        st.info("Security system active")

    elif "fan" in q:
        st.info("Fan running normally")

st.divider()

st.subheader("Live Logs")

st.dataframe(
df.tail(10),
use_container_width=True
)