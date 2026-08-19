import streamlit as st 

def main():
  st.title("Multiplication Table")
  
  number = st.number_input("Enter your number", value=1, min_value=1, max_value=12, key="number")

  if st.button("multiply"):
   for i in range(1,13):
      st.write(f"{number} x {i} = {number * i}")

if __name__ == "__main__":
  main()
