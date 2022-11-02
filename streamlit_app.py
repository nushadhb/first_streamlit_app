
import streamlit as st
import pandas as pd
import requests

#step1 learning..
st.title('My Parents New Healthy Dinner')
st.header('Breakfast Menu')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothies')
st.text('🐔  Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocodo Toast')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#step2 learning.. , import pandas library and read csv file.
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#step3 learning
fruits_selected = st.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#st.text(fruits_to_show)
#st.multiselect("Pick some fruits:",list(my_fruit_list.index))
#st.dataframe(my_fruit_list)
st.dataframe(fruits_to_show)
#step 4 learning
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response)
st.text('fruit wise fruit advise')
# it reads the data from the api in json format into pandas dataframe
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# it loads the data into strealit dataframe 
st.dataframe(fruityvice_normalized)
