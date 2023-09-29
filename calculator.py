import streamlit as st 
res = 0
num1 = st.number_input('Insert First Number:')
print("\n")
num2 = st.number_input('Insert Second Number:')

st.write("""
<style>
.big-font {
    font-size:80px !important;
}
</style>
""", unsafe_allow_html=True)

col1,col2,col3,col4,col5 = st.columns(5)
with col1:
    if st.button("ADD"):
        res = num1 + num2

with col2:
    if st.button("SUB"):
        res = num1 - num2

with col3:
    if st.button("MUL"):
        res = num1 * num2

with col4:
    if st.button("DIV"):
        res = num1 / num2

with col5:
    if st.button("MOD"):
        res = num1 % num2

result = format(res,".2f")
st.write(f'<p class="big-font">Result:{result}</p>',unsafe_allow_html=True)