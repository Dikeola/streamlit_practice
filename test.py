import streamlit as st

def main():
  st.title('Streamlit web app')
  name = st.text_input("Enter your name:")
  st.write(f"Welcome, {name}")

if __name__ == "__main__":
  main()
