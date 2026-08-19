import streamlit as st 

st.title("Streamlit WebApp")

st.session_state.number = st.number_input(value=50, min_value=10,max_value=1000)

if st.button("divide by 5"):
  st.write(f"{st.session_state.number/5}")
