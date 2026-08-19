import streamlit as st
import random

def main():
  st.title("The \"Secret Number\" Guessing Game")

  st.write(random.randint(10))

if __name__ == "__main__":
  main()
