import streamlit as st
import random

def main():
  st.title("The \"Secret Number\" Guessing Game")

  number = random.randint(1,100)

  guess = st.number_input("Guess The number")
  if guess < number:
    st.write("Too Low! Try again.")
    
  elif guess > number:
    st.write("Too High! Try again.")

  else:
    st.write("🎉 Correct! The number was X.")
    st.rerun()

if __name__ == "__main__":
  main()
