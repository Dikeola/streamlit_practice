import streamlit as st 

def main():
  st.title("Streamlit WebApp")
  
  st.session_state.number = st.number_input(value=50)
  
  if st.button("divide by 5"):
    st.write(f"{st.session_state.number/5}")

if __name__ == "__main__":
  main()
