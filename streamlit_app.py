
import streamlit as st
import pandas as pd
import requests
import snowflake.connector

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
#st.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')
#step3 learning
fruits_selected = st.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#st.text(fruits_to_show)
#st.multiselect("Pick some fruits:",list(my_fruit_list.index))
#st.dataframe(my_fruit_list)
st.dataframe(fruits_to_show)
#step 4 learning
#new section to disply fuitwise API response

st.header('Fruityvice Fruit Advise')
fruit_choice = st.text_input('What fruit would you like information about?','kiwi')
st.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#st.text(fruityvice_response)

# it reads the data from the api in json format into pandas dataframe
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# it loads the data into strealit dataframe 
st.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
sql_query="select * from pc_rivery_db.public.fruit_load_list"
#my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
with my_cnx as sf_conn:
     my_data_row=pd.read_sql(sql_query,sf_conn)
     st.dataframe(my_data_row)
     my_data_row.set_index('FRUIT_NAME')
#my_data_row = my_cur.fetchall()
st.text("Hello from Snowflake:")
st.text("The fruit load list contains:")
#st.text(my_data_row)
st.dataframe(my_data_row)
st.text("What fruit would you like to add?")
fruits_add = st.multiselect('Enter your furit wish to add','jackfruit')
#my_data_row = my_data_row.loc[fruits_add]
#my_data_row=my_data_row[my_data_row['FRUIT_NAME'].isin([fruits_add])]
st.text('Thanks for adding the fruit!',fruits_add)
#st.dataframe(fruits_add)
