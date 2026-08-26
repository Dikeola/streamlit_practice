import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
  st.title("CSV Data Explorer")
  fle = st.file_uploader("Choose a CSV file:", type='csv')
  if fle is not None:
    df = pd.read_csv(fle)
    st.DataFrame(df, use_container_width=True)
if __name__ == "__main__":
  main()
