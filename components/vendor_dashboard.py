import streamlit as st
from data.sample_data import GROUP_ORDERS
from utils.helpers import update_order_status, time_remaining

def vendor_view():
    st.subheader("🧑‍🍳 Join Group Orders")

    for order in GROUP_ORDERS:
        update_order_status(order)
        if order['status'] != 'open':
            continue

        st.markdown(f"### 🛍️ {order['product']}")
        st.write(f"Price: ₹{order['price_per_unit']}/kg")
        st.write(f"Required: {order['min_qty']}kg")
        st.write(f"Current: {order['committed']}kg")
        st.write(f"⏳ Time left: {time_remaining(order['expiry'])}")

        progress = order['committed'] / order['min_qty']
        st.progress(progress if progress <= 1 else 1.0)

        qty = st.number_input("Add your quantity:", min_value=1, key=f"input_{order['id']}")
        if st.button("Join Order", key=f"btn_{order['id']}"):
            order['committed'] += qty
            st.success("✅ Added to group order!")

        st.divider()
