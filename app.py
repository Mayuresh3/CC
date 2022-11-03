import streamlit as st

st.title("Cloud Computing")

num = st.number_input('Pick a number', 0, 100)
if(num>90):
    st.write("O")
    st.balloons()
elif(num>80):
    st.write("A")
    st.balloons()
elif(num>70):
    st.write("B")
    st.balloons()
elif(num>60):
    st.write("C")
    st.snow()
elif(num>50):
    st.write("D")
    st.snow()
elif(num>40):
    st.write("E")
    st.snow()
else:
    st.warning("Failed")
