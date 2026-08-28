import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def main():
  st.title("CSV Data Explorer Version_2")

  fle = st.file_uploader("Upload your file:", type='csv')
  
  st.sidebar.header("Filter Options")
  if fle is not None:
    df = pd.read_csv(fle)
    columns = st.sidebar.selectbox("Select the Columns:", df.columns)
    st.dataframe(fle, use_container_width=True)
if __name__ == "__main__":
  main()
