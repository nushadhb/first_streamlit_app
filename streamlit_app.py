
import streamlit as st
import pandas as pd
import requests
import snowflake.connector

#step1 learning..
streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothies')
streamlit.text('🐔  Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocodo Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#step2 learning.. , import pandas library and read csv file.
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_listreamlit.set_index('Fruit')
#step3 learning
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_listreamlit.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_listreamlit.loc[fruits_selected]
#streamlit.text(fruits_to_show)
#streamlit.multiselect("Pick some fruits:",list(my_fruit_listreamlit.index))
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)
#step 4 learning
#new section to disply fuitwise API response

streamlit.header('Fruityvice Fruit Advise')
fruit_choice = streamlit.text_input('What fruit would you like information about?','kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response)

# it reads the data from the api in json format into pandas dataframe
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# it loads the data into strealit dataframe 
streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
