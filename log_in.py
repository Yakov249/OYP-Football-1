import streamlit as st
import json
def read_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
def authenticate(username, password):
    users = read_users()
    if username in users and users[username] == password:
        return True
    return False
def set_clicked():
    st.session_state.clicked = True
def set_page(page_name):
    st.session_state.page = page_name
def log_in_page():
    st.title("Log in Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type = "password")
    if st.button("Log in"):
        if authenticate(username, password):
            st.success("Logged in successfully")
            st.button(("Continue"), on_click = set_page, args = ("Player database",))
            st.button(("Head back to the home page"), on_click = set_page, args = ("main",))
            return True
        else:
            st.error("Invalid username or password")
