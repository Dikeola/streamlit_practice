import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def main():
  st.title("CSV Data Explorer Version_2")

  fle = st.file_explorer("Upload your file:", type='csv')
  choice = st.sidebar.selectbox('choice',['yes','no'])
  if fle is not None:
    st.dataframe(fle, use_container_width=True)
if __name__ == "__main__":
  main()
