import streamlit as st 

def main():
  st.title("Convert text to a list")
  
  text = st.text_input("Enter your text", key="text")
  
  
  if st.button("convert"):
    st.write(list(text))

if __name__ == "__main__":
  main()
