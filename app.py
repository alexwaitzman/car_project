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

# looping over column names and replacing missing values in colums paint_colour and is_4wd with 'unknown'
columns_to_replace = ['paint_color','is_4wd']
for column in columns_to_replace:
   df[column] = df[column].fillna('unknown')
   
#Filling in the NaN values in model_year with median using group by model and model_year
df['model_year'] = pd.to_numeric(df['model_year'], errors='coerce')
df['model_year'] = df['model_year'].astype(float).fillna(df.groupby(['model'])['model_year'].transform('median'))
print(df['model_year'])

#Filling in the NaN values in cylinders with mode using group by model and model_year
df['cylinders'] = pd.to_numeric(df['cylinders'], errors='coerce')
df['cylinders'] = df['cylinders'].fillna(df.groupby(['model','model_year'])['cylinders'].transform(pd.Series.mode))
print(df['cylinders'])

#Filling in the NaN values in odometer with mode using group by model,model_yearбензу and condition
df['odometer'] = pd.to_numeric(df['odometer'], errors='coerce')
df['odometer'] = df['odometer'].fillna(df.groupby(['model','model_year','type','condition'])['odometer'].transform('median'))
print(df['odometer'])


#checking for duplicates
df.duplicated().sum()
#droping duplicates
df=df.drop_duplicates()
#checking for duplicates again
df.duplicated().sum()

#creating slider for the price range and checkbox for the cars that have less then 10 years since production 
st.caption('Choose your parameters here')
price_range = st.slider(
     "What is your price range?",
     value=(1, 375000))

actual_range=list(range(price_range[0],price_range[1]+1))

not_old_cars = st.checkbox('Only cars less then 10 years old')

if not_old_cars:
    filtered_data=df[df.price.isin(actual_range)]
    df.model_year = df.model_year.astype(str)
    filtered_data=filtered_data[df.model_year>='2010']
else:
    filtered_data=df[df.price.isin(actual_range)]
    
#scatterplot with a split by price and condition

fig = px.scatter(filtered_data, title="Split of cars by price and condition", x="price", y="condition")           
st.plotly_chart(fig)

#Conclusion from the scatterplot with a split by price and condition
st.write('Conclusion about the depandancy of price from condition:')
st.write('1) Absolute majority of the cars with new, like new, excellent and good condition have pretty much the same prices')
st.write('2) The prices for new, like new, excellent and good condition cars are mostly less then 60 000 $')
st.write('3) The prices for salvage and fair condition cars are mostly less then 20 000 $')

#Histogram showing the average price by model
fig2 = px.histogram(filtered_data, title="Average price by model", x="model", y="price",histfunc="avg")
st.plotly_chart(fig2)

st.write('Conclusion about the average prices by the model:')
st.write('1) The average prices of most of the models are below 10 000 $')
st.write('2) The most expensive model is Mercedes-benz Sprinter 2500 with the average price of 34900$')

st.header('Overall Conclusion')
st.write('We found out that:')
st.write('1) Absolute majority of the cars with new, like new, excellent and good condition have pretty much the same prices')
st.write('2) The prices for new, like new, excellent and good condition cars are mostly less then 60 000 $')
st.write('3) The prices for salvage and fair condition cars are mostly less then 20 000 $')
st.write('4) The average prices of most of the models are below 10 000 $')
st.write('5) The most expensive model is Mercedes-benz Sprinter 2500 with the average price of 34900$')