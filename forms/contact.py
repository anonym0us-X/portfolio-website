import streamlit as st
import re
import requests


WEBHOOK_URL = ""

def is_email_valid(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with st.form("contatct_form"):
        st.write("This form feature is yet to be functional, please find the contact details at the contact page for now 😞.")
        first_name = st.text_input("First Name: ")
        last_name = st.text_input("Last Name:")
        email = st.text_input("Email: ")
        message = st.text_area("Message: ")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if not WEBHOOK_URL:
                st.error("Email services are not configured, please try later" , icon= "💌")
                st.stop()
            if not first_name:
                st.error("Please enter your first name")
                st.stop()
            if not last_name:
                st.error("Please enter your first name")
                st.stop()
            if not email:
                st.error("Please enter your email")
                st.stop()
            if not is_email_valid(email):
                st.error("Please enter valid email")
                st.stop()
            if not message:
                st.error("Please enter your message")
                st.stop()


            data = {"email": email, "first_name": first_name,"last_name":last_name, "message": message}
            response = requests.post(WEBHOOK_URL, json = data)

            if response.status_code == 200:
                st.success("Your message has been sent successfully!🎉", icon = "💬")
                        
            else:
                st.error("There was an error sending your message!", icon = "😨")