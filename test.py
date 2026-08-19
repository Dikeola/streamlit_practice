import streamlit as st

def main():
  st.title('Streamlit web app')
  counter = 0
  if st.button(""):
    st.write(f"count {counter+1}")

if __name__ == "__main__":
  main()
