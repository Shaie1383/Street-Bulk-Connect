import time
import streamlit as st
from datetime import datetime

def update_order_status(order):
    if datetime.now() >= order['expiry']:
        order['status'] = 'closed'
    else:
        order['status'] = 'open'

def time_remaining(expiry_time):
    now = datetime.now()
    remaining = expiry_time - now
    if remaining.total_seconds() <= 0:
        return "Expired"
    mins, secs = divmod(remaining.total_seconds(), 60)
    return f"{int(mins)}m {int(secs)}s"

def countdown_timer(expiry_time):
    placeholder = st.empty()
    now = datetime.now()
    remaining = expiry_time - now
    if remaining.total_seconds() <= 0:
        placeholder.markdown("⏰ **Order Closed!**")
    else:
        mins, secs = divmod(remaining.total_seconds(), 60)
        placeholder.markdown(f"⏳ Time Left: **{int(mins)}m {int(secs)}s**")

def animated_progress(current, target):
    percent = min(100, int((current / target) * 100))  # Prevent overflow
    progress_bar = st.progress(0)
    for i in range(percent + 1):
        time.sleep(0.01)
        progress_bar.progress(i)