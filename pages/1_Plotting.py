import streamlit as st
import pandas as pd 
import numpy as np 
import seaborn as sns 
import os
import plotly.express as px

st.set_page_config(
      page_title= 'Data Visualisation'

)

st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)
status_text = st.sidebar.empty()

progress_bar = st.sidebar.progress(0)

absolute_path = os.path.abspath(os.path.dirname('housing_price_dataset.csv'))


df = pd.read_csv(absolute_path + '/housing_price_dataset.csv')
st.dataframe(df)

fig = px.pie(df, names= 'Neighborhood', values= 'Price')

st.plotly_chart(fig)












"""
Neighborhood = st.multiselect(
    "Choose Countries", df['Neighborhood'].unique(), ["Urban"]
)
if not Neighborhood:
        st.error("Please select at least one Neighborhood.")
else:
   st.dataframe(df)
"""