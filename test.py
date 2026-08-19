import streamlit as st

def main():
  st.title('Streamlit web app')
  counter = 0
  if st.button("Add 1"):
    st.write(f"count {counter+1}")

if __name__ == "__main__":
  main()
