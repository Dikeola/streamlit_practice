import streamlit as st

def main():
  st.title("The 3-Step Story")
  if "screen" not in st.session_state:
    st.session_state.screen = 1

  if st.session_state.screen == 1:
    st.write("You are standing in a dark forest. There is a path to the left and a cave to the right.")
    
    if st.button("Go Left"):
      st.session_state.screen = 2  
    if st.button("Go Right"):
      st.session_state.screen = 3
      
  if st.session_state.screen == 2:
    st.write("You walked left and found a treasure chest! You Win!")
    if st.button("Play Again!"):
      st.session_state.screen=1
      st.rerun()
  if st.session_state.screen == 3:
    st.write("You walked right and fell into a trap! Game Over.")
    if st.button("Play Again!"):
      st.session_state.screen=1
      st.rerun()

  
if __name__ == "__main__":
  main()
