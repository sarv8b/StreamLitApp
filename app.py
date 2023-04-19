import streamlit as st

def largest_of_three(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

st.title("Largest of Three Numbers")
st.write("Enter three numbers below:")

a = st.number_input("First number:", value=0)
b = st.number_input("Second number:", value=0)
c = st.number_input("Third number:", value=0)

if st.button("Calculate"):
    result = largest_of_three(a, b, c)
    st.write("The largest number is:", result)
