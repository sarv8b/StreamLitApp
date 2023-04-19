import streamlit as st 

A=st.number_input(int(input("Enter first number: ")))
B=st.number_input(int(input("Enter second number: ")))
C=st.number_input(int(input("Enter third number: ")))
if (A >= B) and (A >= C):
 largest = A
elif (B >= A) and (B >= C):
 largest = B
else:
 largest = C
st.write("The largest number between",A,",",B,"and",C,"is",largest)
