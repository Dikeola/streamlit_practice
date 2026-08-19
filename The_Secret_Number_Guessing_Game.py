import streamlit as st
import random

def main():
  st.title("The \"Secret Number\" Guessing Game")
  if st.button("Random"):
    
    st.write(random.randint(1,10))

if __name__ == "__main__":
  main()
