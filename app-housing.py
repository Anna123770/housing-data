import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

st.title('Califprnia Housing Data (1990) By Yifei Tang')
df= pd.read_csv('housing.csv')

# filter by house price
house_price_filter=st.slider('Median House Price',0,500001,200000)
df=df[df.median_house_value>=house_price_filter]

st.subheader('See more filters in the sidebar:')
st.map(df)
st.subheader('Histogram of the Median House Value')
fig,ax=plt.subplots(figsize=(70,50))
df.median_house_value.hist(bins=30)
st.pyplot(fig)

#filter by location type
loaction_type_filter=st.sidebar.multiselect('Choose the location type:',df.ocean_proximity.unique(),df.ocean_proximity.unique())
df=df[df.ocean_proximity.isin(loaction_type_filter)]

#filter by income level
income_level_filter=st.sidebar.radio('Choose income level',('Low','Medium','High'))
if income_level_filter is 'Low':
    df=df[df.median_income<=2.5]
elif income_level_filter is 'High':
    df=df[df.median_income>=4.5]
else:
    df=df[df.median_income>2.5 and df.median_income<4.5]

