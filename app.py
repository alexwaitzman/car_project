import pandas as pd
import streamlit as st
import plotly.express as px
#creating a header
st.header('Reading info on our :purple[dataset] :sunglasses:')
#creating a subheader
st.write("""
### Head of data
""")
#reading the file
df=pd.read_csv('vehicles_us.csv')
st.table(df.head())

#creating slider for the price range and checkbox for excellent condition
st.caption(':red[Choose your parameters here]')
price_range = st.slider(
     "What is your price range?",
     value=(1, 375000))

actual_range=list(range(price_range[0],price_range[1]+1))

excellent_condition = st.checkbox('only excellent condition')

if excellent_condition:
    filtered_data=df[df.price.isin(actual_range)]
    filtered_data=filtered_data[df.condition=='excellent']
else:
    filtered_data=df[df.price.isin(actual_range)]
    
#scatterplot
st.write('Here are your options with a split by price and condition')

fig = px.scatter(filtered_data, x="price", y="condition")           
st.plotly_chart(fig)

st.write('Distribution of vehicle types by model')
fig2 = px.histogram(filtered_data, x='model', y="type")
st.plotly_chart(fig2)