import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
  st.title("CSV Data Explorer")
  fle = st.file_uploader("Choose a CSV file:", type='csv')
if __name__ == "__main__":
  main()
