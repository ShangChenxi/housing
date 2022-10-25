import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

plt.style.use('seaborn')
st.title('California Housing Data (1990) by Chenxi Shang')
df = pd.read_csv('housing.csv')

price_filter = st.slider('Median House Price', 0, 500001, 200000)

location_type_filter = st.sidebar.multiselect('Choose the location type', df.ocean_proximity.unique(), df.ocean_proximity.unique())

income_filter = st.sidebar.radio('Choose', ('Low', 'Medium', 'High'))

df = df[df.median_house_value >= price_filter]

df = df[df.ocean_proximity.isin(location_type_filter)]

if income_filter is None:
    pass
elif income_filter == 'Low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
else:
    df = df[df.median_income > 4.5]

st.map(df)


st.subheader('Histogram of the Median House Value')


fig, ax = plt.subplots()
df.median_house_value.hist(bins=30)

st.pyplot(fig)