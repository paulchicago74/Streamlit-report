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




metric = 100 / 10

# sample data
df = pd.DataFrame({
    'first column': [metric, metric * 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df

chart = st.line_chart(df)
# plot the pivoted dataframe; if the column names aren't colors, remove color=df.columns



  
