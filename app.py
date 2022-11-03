import streamlit as st

st.title("Cloud Computing")

num = st.number_input('Pick a number', 0, 100)
if(num>90):
    st.write("O")
elif(num>80):
    st.write("A")
elif(num>70):
    st.write("B")
elif(num>60):
    st.write("C")
elif(num>50):
    st.write("D")
elif(num>40):
    st.write("E")
else:
    st.write("Fail")
