from sign_up import sign_up_page
from log_in import log_in_page
from player_database import player_database_page
from PIL import Image
import streamlit as st
st.set_page_config(page_title = "OYP Football player database", page_icon = ":soccer:", layout = "wide")
def click_button():
    st.session_state.clicked = True
def initialize_session_state():
    if "clicked" not in st.session_state:
        st.session_state.clicked = False
def click_log_in_button():
    st.session_state.page = "Log in"
    st.session_state.clicked = True
def click_sign_up_button():
    st.session_state.page = "Sign up"
    st.session_state.clicked = True
def page_management():
    initialize_session_state()
    if "page" not in st.session_state:
        st.session_state.page = "main"
    if st.session_state.page == "main":
        main()
    elif st.session_state.page == "Sign up":
        sign_up_page()
    elif st.session_state.page == "Log in":
        log_in_page()
    elif st.session_state.page == "Player database":
        player_database_page()
def main():
    with st.container():
        st.title("OYP Football player database :soccer:")
        st.header("Hello and welcome to OYP Football by Osher Lakau and Yakov Markov :wave:")
        st.subheader("Are you a Football fan? Are you somewhere connected to this beautiful sport?")
        st.subheader("In our project we are building a website where you can search about your favorite football players information!")
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Who are we?")
            st.write("We study in Tichon Hadera in the 10th grade.")
            st.write("We are making a school project in computer science that called OYP Football.")
        with right_column:
            st.image(Image.open("image/Tichon Hadera.jpg"))
    with st.container():
        st.write("---")
        st.header("Hope you will enjoy your time in here!")
        left_column, right_column = st.columns(2)
        with left_column:
            st.image(Image.open("image/Messi.webp"))
        with right_column:
            st.image(Image.open("image/Ronaldo.webp"))
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.button("Don't have an account? Sign up", on_click = click_sign_up_button)
        with right_column:
            st.button("Already have an account? Log in", on_click = click_log_in_button)
page_management()
