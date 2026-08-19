import streamlit as st 

def main():
  st.title("Streamlit WebApp")
  
  number = st.number_input("Enter your number", value=50, step=5, key='number')
  
  if st.button("divide by 5"):
    st.write(f"{st.session_state.number/5}")
    st.session_state.number = st.session_state.number/5

if __name__ == "__main__":
  main()
