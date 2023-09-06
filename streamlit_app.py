
#creat the gitgup repo and code 
#login to https://streamlit.io/ and create the application link to the gitgub repo. 
#next run the application  ( deploy the apolicaiton, it will automatically taken care of all o ther dependencies)
# once you modify the code, refres the streamlit.ip/page .
import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

#declare common varibales
fruit_table=st.secreats["db"].fruit_table
st.text(fruit_table)
exit(0)
print(
def sf_connect():
     my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
     return my_cnx
def page_refresh():
     my_cnx = sf_connect()
     my_cur=my_cnx.cursor()
     my_cur.execute("insert into pc_rivery_db.public.fruit_load_list_old values('from strealimit')")
def  get_fruityvice_data(this_fruit_choice):
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
     #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
     #st.text(fruityvice_response)
     # it reads the data from the api in json format into pandas dataframe
     fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
     # it loads the data into strealit dataframe 
     return fruityvice_normalized 
def insert_row_snowflake(new_fruit):
     my_cnx = sf_connect()
     my_cur = my_cnx.cursor()
     my_cur.execute("insert into pc_rivery_db.public.fruit_load_list_old values('" + new_fruit +"')")
     my_cur.close()
     return "thanks for adding new fruit " + new_fruit
def get_the_fruit_load_list():
    my_cnx=sf_connect()
    sql_query="select * from pc_rivery_db.public.fruit_load_list_old;"
    #my_cur.execute("select * from pc_rivery_db.public.fruit_load_list_old")
    with my_cnx as sf_conn:
        my_data_row=pd.read_sql(sql_query,sf_conn)
    return my_data_row

#step1 learning..
st.title('My Parents New Healthy Dinner!!!')
st.header('Breakfast Menu')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothies')
st.text('🐔  Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocodo Toast')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#st.stop()
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
try: 
    fruit_choice = st.text_input('What fruit would you like information about?')
    if not fruit_choice:
        st.error('Please select a fruit to get information.')
    else:
        back_from_function=get_fruityvice_data(fruit_choice)
        st.dataframe(back_from_function)
except URLError as e:
        st.error(e)
#st.stop()
#st.text("The fruit load list contains:")
st.text("View our fruit list - Add your fvourite!")
if st.button('Get Fruit List'):
    my_data_row = get_the_fruit_load_list()
    st.dataframe(my_data_row)
#st.text(my_data_row)
st.text("What fruit would you like to add?")
add_my_fruit = st.text_input('Enter the fruit you wish to add?')
if st.button('Add fruit to the list'):
    back_from_fuction=insert_row_snowflake(add_my_fruit)
    st.write(back_from_fuction)

#my_data_row = my_data_row.loc[fruits_add]
#my_data_row=my_data_row[my_data_row['FRUIT_NAME'].isin([fruits_add])]

#st.dataframe(fruits_add)
