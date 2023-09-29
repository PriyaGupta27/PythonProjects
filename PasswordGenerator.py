import streamlit as st
import random
import string

st.write("""
<style>
.big-font {
    font-size:40px !important;
}
</style>
""", unsafe_allow_html=True)

password_length = st.number_input("Password length",step=0)

def generate_random_string(n):
    symbol = string.ascii_letters + string.digits + string.octdigits + string.punctuation
    pwd = ''.join(random.choice(symbol) for i in range(n))
    return pwd


if password_length > 0:
    st.write(f'<p class="big-font">Your generated password:</p>',unsafe_allow_html=True)
    st.write(f'<p class="big-font">{generate_random_string(password_length)}</p>',unsafe_allow_html=True)


