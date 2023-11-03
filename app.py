import pandas as pd
import streamlit as st
import plotly.express as px
st.header('Reading info on our :purple[dataset] :sunglasses:')
st.write("""
### Head of data
""")
df=pd.read_csv('vehicles_us.csv')
st.table(df.head())

