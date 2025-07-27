# app.py

import streamlit as st
from components.login import login
from components.supplier_dashboard import supplier_view
from components.vendor_dashboard import vendor_view

# Load custom styles
def inject_styles():
    try:
        with open("assets/styles.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("⚠️ Custom styles not found. Skipping style injection.")

# Inject styles
inject_styles()

# Show logo and heading
st.image("assets/logo.jpg", width=90)
st.markdown("<h1 style='margin-top: -15px;'>🛒 Street Bulk Connect</h1>", unsafe_allow_html=True)

# Updated login logic
username, role = login()

# Route to dashboards
if role == "Supplier":
    supplier_view()
elif role == "Vendor":
    vendor_view()
else:
    st.info("Please select a role to continue.")
