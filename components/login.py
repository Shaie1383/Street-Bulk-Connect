import streamlit as st
from data.sample_data import USERS

def login():
    if "show_signup" not in st.session_state:
        st.session_state.show_signup = False

    # ✳️ If signup selected
    if st.session_state.show_signup:
        return signup_view()

    # 🔐 Login Form
    st.sidebar.title("Login")

    role = st.sidebar.selectbox("Login as", ["Vendor", "Supplier"])
    possible_users = {k: v for k, v in USERS.items() if v["role"] == role.lower()}
    usernames = list(possible_users.keys())

    username = None
    if usernames:
        username = st.sidebar.selectbox("Select your username", usernames)
        user = USERS[username]
        st.sidebar.success(f"Logged in as **{user['name']}** ({user['role'].capitalize()})")
    else:
        st.sidebar.info(f"No {role}s found.")

    # ✅ Always show Sign Up option
    st.sidebar.markdown("---")
    st.sidebar.markdown("Don't have an account?")
    if st.sidebar.button("➕ Sign Up"):
        st.session_state.show_signup = True
        st.experimental_rerun()

    if username:
        return username, possible_users[username]["role"].capitalize()
    else:
        return None, None

# 🔄 Signup Flow
def signup_view():
    st.sidebar.title("Sign Up")

    new_username = st.sidebar.text_input("Choose a username")
    name = st.sidebar.text_input("Full Name")
    email = st.sidebar.text_input("Email")
    role = st.sidebar.selectbox("Sign up as", ["Vendor", "Supplier"])

    if st.sidebar.button("Create Account"):
        if new_username in USERS:
            st.sidebar.error("❌ Username already exists.")
        elif not new_username or not name or not email:
            st.sidebar.warning("⚠️ Please fill in all fields.")
        else:
            USERS[new_username] = {"role": role.lower(), "name": name}
            st.sidebar.success("✅ Account created!")
            st.session_state.show_signup = False
            st.experimental_rerun()

    if st.sidebar.button("🔙 Back to Login"):
        st.session_state.show_signup = False
        st.experimental_rerun()

    return None, None
