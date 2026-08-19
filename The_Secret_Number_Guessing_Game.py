import streamlit as st
import random

def main():
  st.title("The \"Secret Number\" Guessing Game")

  number = random.randint(1,100)

  guess = st.text_input("Guess The number")
  if int(guess) < number:
    st.write("Too Low! Try again.")
    
  elif int(guess) > number:
    st.write("Too High! Try again.")

  else:
    st.write("🎉 Correct! The number was X.")
    
  if st.button("Random"):
    st.write(random.randint(1,10))

if __name__ == "__main__":
  main()
