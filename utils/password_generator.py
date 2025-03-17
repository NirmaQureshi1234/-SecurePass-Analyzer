import random
import string
import streamlit as st

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

from utils.password_generator import generate_password

# Add a button to generate a password
if st.button("Generate Strong Password"):
    generated_password = generate_password()
    st.text_input("Generated Password", generated_password, disabled=True)