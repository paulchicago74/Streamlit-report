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
import altair as alt

Temp = 150
Tref = 110
Zref = 10
Time = 25
Dvalue = 10

Fvalue0 = 0
Fvalue1 = (Fvalue0 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/10) - 0))
Fvalue2 = (Fvalue1 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/9) - (Time/10)))
Fvalue3 = (Fvalue2 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/8) - (Time/9)))
Fvalue4 = (Fvalue3 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/7) - (Time/8)))
Fvalue5 = (Fvalue4 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/6) - (Time/7)))
Fvalue6 = (Fvalue5 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/5) - (Time/6)))
Fvalue7 = (Fvalue6 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/4) - (Time/5)))
Fvalue8 = (Fvalue7 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/3) - (Time/4)))
Fvalue9 = (Fvalue8 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/2) - (Time/3)))
Fvalue10 = (Fvalue9 + (10 ** ((Temp - Tref)/Zref) + (10 ** ((Temp - Tref)/Zref)))/2*((Time/1) - (Time/2)))

Dvalue0 = 0
Dvalue1 = Fvalue1 / Dvalue
Dvalue2 = Fvalue2 / Dvalue
Dvalue3 = Fvalue3 / Dvalue
Dvalue4 = Fvalue4 / Dvalue
Dvalue5 = Fvalue5 / Dvalue
Dvalue6 = Fvalue6 / Dvalue
Dvalue7 = Fvalue7 / Dvalue
Dvalue8 = Fvalue8 / Dvalue
Dvalue9 = Fvalue9 / Dvalue
Dvalue10 = Fvalue10 / Dvalue

#D= Fvalue / Dvalue

metric = 100 / 10

# sample data
df = pd.DataFrame({
    'F-value': [Fvalue0, Fvalue1, Fvalue2, Fvalue3, Fvalue4, Fvalue5, Fvalue6, Fvalue7, Fvalue8, Fvalue9, Fvalue10],
    #'D-value': [Dvalue0, Dvalue1, Dvalue2, Dvalue3, Dvalue4, Dvalue5, Dvalue6, Dvalue7, Dvalue8, Dvalue9, Dvalue10]
})

#df

df2 = pd.DataFrame({
    #'F-value': [Fvalue0, Fvalue1, Fvalue2, Fvalue3, Fvalue4, Fvalue5, Fvalue6, Fvalue7, Fvalue8, Fvalue9, Fvalue10],
    'D-value': [Dvalue0, Dvalue1, Dvalue2, Dvalue3, Dvalue4, Dvalue5, Dvalue6, Dvalue7, Dvalue8, Dvalue9, Dvalue10]
})

df2


#chart = st.line_chart(df)
#chart = st.line_chart(df2)
# plot the pivoted dataframe; if the column names aren't colors, remove color=df.columns

df2 = alt.Chart(df).mark_circle().encode({
    #'F-value': [Fvalue0, Fvalue1, Fvalue2, Fvalue3, Fvalue4, Fvalue5, Fvalue6, Fvalue7, Fvalue8, Fvalue9, Fvalue10],
    'D-value': [Dvalue0, Dvalue1, Dvalue2, Dvalue3, Dvalue4, Dvalue5, Dvalue6, Dvalue7, Dvalue8, Dvalue9, Dvalue10]
})
#alt.Chart(df).mark_circle().encode(
    
st.altair_chart(df2)
