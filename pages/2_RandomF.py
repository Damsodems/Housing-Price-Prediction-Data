#import
import streamlit as st 
from sklearn.ensemble import RandomForestRegressor
import pandas as pd 
import os
from sklearn.model_selection import train_test_split

#set pages
st.set_page_config(
    page_title= "Interactive Random Forest Regressor"
)

st.markdown("# Interactive Random Forest Regressor")

st.sidebar.markdown('# Interactive')
estimators = st.sidebar.slider("Number of estimator", 1, 500, 250, 10)

# get data
absolute_path = os.path.abspath(os.path.dirname('housing_price_dataset.csv'))
df = pd.read_csv(absolute_path + '/housing_price_dataset.csv')

#ML preprocessing
Y = df['Price']
X = df.drop('Price', axis = 1)
X = pd.get_dummies(X, columns= ['Neighborhood'], dtype=int ) #One hot encoding

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size= 0.20, random_state= 35 )



rf = RandomForestRegressor(max_depth= 3, random_state= 50, n_estimators= )



