import pandas as pd
import streamlit as st
import plotly.express as px
#creating a header
st.header('Investigation of car advertisement market in US')
#creating a project description
st.write('In this app we will investigate dependancy of the car price from a condition and from a model')

#reading the file
df=pd.read_csv('vehicles_us.csv')

#creating a subheader
st.write("""
### Head of data
""")
st.table(df.head())

#Filling in missing values in the data
df.isna().sum()

# looping over column names and replacing missing values with 'unknown'
columns_to_replace = ['model_year','cylinders','odometer','paint_color','is_4wd']
for column in columns_to_replace:
   df[column] = df[column].fillna('unknown')

#checking for duplicates
df.duplicated().sum()
#droping duplicates
df=df.drop_duplicates()
#checking for duplicates again
df.duplicated().sum()

#creating slider for the price range and checkbox for excellent condition
st.caption('Choose your parameters here')
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
    
#scatterplot  with a split by price and condition
st.write('Here are your options with a split by price and condition')

fig = px.scatter(filtered_data, x="price", y="condition")           
st.plotly_chart(fig)

#Histogram showing the average price by model
st.write('Average price by model')
fig2 = px.histogram(filtered_data, x="model", y="price",histfunc="avg")
st.plotly_chart(fig2)

st.header('Conclusion')
st.write('We found out that:')
st.write('1) The prices of the cars with new, excellent, like new and good conditions are mostly before 100K')
st.write('2) The average prices for most models are below 10 000 $')