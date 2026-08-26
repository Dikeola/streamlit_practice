import matplotlib.pyplot as plt
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn.datasets import fetch_20newsgroups
import pandas as pd

news = fetch_20newsgroups(subset='train', remove=('header','quotes','footer'), shuffle=True)
news_df = pd.DataFrame({"text": news.data, 'labels':news.target})
tfidf = TfidfVectorizer()

def main():
  st.title("Sentiment Analyzer")
  text = st.text_input("Enter your text")
  tf_v = tfidf.fit_transform(pd.Series(text))

  if st.button("Generate Sentiment Table"):
    st.write(f"{pd.DataFrame(tf_v.toarray(), columns= tf_v.get_feature_names_out())}")
  
if __name__ == "__main__":
  main()
