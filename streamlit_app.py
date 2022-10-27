
import streamlit as st
import pandas as pd
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
#step3 learning
st.multiselect("Pick some fruits:",list(my_fruit_list.index))
st.dataframe(my_fruit_list)

