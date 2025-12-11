import streamlit as st

st.title("This is a title")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
def pangkat(x, n):
    if n == 0:
        return 1
    f
    if n < 0:
        return 1 / pangkat(x, -n)
    return x * pangkat(x, n - 1)

#  penggunaan
print(pangkat(2, 5))   
print(pangkat(3, 3))   
print(pangkat(2, -3))   
