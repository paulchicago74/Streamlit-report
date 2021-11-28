import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe
import pandas as pd
import numpy as np
import streamlit_gchart as gchart
import plotly.offline as offline
import plotly.graph_objs as go

Temp = 150
Tref = 165
Zref = 10
Time = 25
Dvalue = 10

Fvalue1 = (10 ** ((Temp - Tref)/Zref))/1 * Time/10
Fvalue2 = Fvalue1 + 2 * (10 ** ((Temp - Tref)/Zref))/1 * Time/9

#D= Fvalue / Dvalue

metric = 100 / 10

# sample data
df = pd.DataFrame({
    'first column': [Fvalue1, Fvalue2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df

chart = st.line_chart(df)
# plot the pivoted dataframe; if the column names aren't colors, remove color=df.columns



  
