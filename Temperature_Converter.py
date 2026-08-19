import streamlit as st

def main():
  st.title("Temperature Converter")
  cat = st.sidebar.selectbox("Select a Category", ['Celsius',"Kelvin","Fahrenheit"])
  st.write(cat)
if __name__ == "__main__":
  main()
