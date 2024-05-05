import streamlit as st
import json
def read_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
def write_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file)
def set_page(page_name):
    st.session_state.page = page_name
def sign_up_page():
    st.title("Sign up page")
    username = st.text_input("Username")
    password = st.text_input("Password", type = "password")
    if st.button("Sign up"):
        users = read_users()
        if username in users:
            st.error("Username already taken")
        else:
            users[username] = password
            write_users(users)
            st.success("User registered successfully")
            st.button(("Head back to the home page"), on_click = set_page, args = ("main",))
            return True
