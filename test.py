import streamlit as st

def main():
  st.title('Streamlit web app')
  if "counter" not in st.session_state:
    st.session_state.counter = 0
  if st.button("Add 1"):
    st.session_state.counter +=1
  st.write(f"count {st.session_state.counter+1}")

if __name__ == "__main__":
  main()
