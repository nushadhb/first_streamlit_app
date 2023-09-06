import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
st.slider("This is a slider", 0, 100, (25, 75))
st.divider()
naushad 
