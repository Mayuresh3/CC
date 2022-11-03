import streamlit as st

st.write("Cloud Computing")

num = st.number_input('Pick a number', 0, 100)
if(num>90):
    st.write("O")
elif(num>80):
    st.write("A+")
elif(num>70):
    st.write("A")
elif(num>60):
    st.write("B+")
elif(num>50):
    st.write("B")
else:
    print("Fail")
