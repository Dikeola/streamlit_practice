import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def main():
  st.title("CSV Data Explorer Version_2")

  fle = st.file_uploader("Upload your file:", type='csv')
  
  if fle is not None:
    df = pd.read_csv(fle)
    
    st.sidebar.header("Filter Options")
    columns = st.sidebar.selectbox("Select the Columns:", ['1','2'])
    st.dataframe(fle, use_container_width=True)
if __name__ == "__main__":
  main()
