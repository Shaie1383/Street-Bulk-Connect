import streamlit as st
from data.sample_data import GROUP_ORDERS
from utils.helpers import update_order_status, time_remaining, animated_progress, countdown_timer

def supplier_view():
    st.subheader("📦 Your Product Listings")

    for order in GROUP_ORDERS:
        update_order_status(order)
        st.markdown(f"### 🛍️ {order['product']}")
        st.write(f"💰 Price per unit: ₹{order['price_per_unit']}/kg")
        st.write(f"📦 Required: {order['min_qty']}kg")
        st.write(f"👥 Committed: {order['committed']}kg")

        animated_progress(current=order['committed'], target=order['min_qty'])
        countdown_timer(order['expiry'])

        if order['status'] != 'open':
            st.markdown(f"### ✅ Order {order['status'].capitalize()}")
        st.divider()
