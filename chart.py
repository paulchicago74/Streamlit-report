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
Tref = 150
Zref = 10
Time = 25
Dvalue = 10

Fvalue0 = 0
Fvalue1 = (Fvalue0 + (10 ** ((Temp - Tref)/Zref)) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/10) - 0 ))
Fvalue2 = (Fvalue1 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/9) - (Time/10)))
Fvalue3 = (Fvalue1 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time) - (Time/9)))
#D= Fvalue / Dvalue

metric = 100 / 10

# sample data
df = pd.DataFrame({
    'first column': [Fvalue0, Fvalue1, Fvalue2, Fvalue3, 4],
    'second column': [0, 10, 20, 30, 40]
})

df

chart = st.line_chart(df)
# plot the pivoted dataframe; if the column names aren't colors, remove color=df.columns



  
