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


st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")
st.title("🎓 Diploma PDF Generator")

st.write(
    "This app shows you how you can use Streamlit to make a PDF generator app in just a few lines of code!"
)

left, right = st.columns(2)

right.write("Here's the template we'll be using:")

#right.image("template.png", width=300)

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.html")


left.write("Fill in the data:")

form = left.form("template_form")
metric = 100 / 10

# sample data
df = pd.DataFrame({
    'first column': [metric, metric * 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df

chart = st.line_chart(df)
# plot the pivoted dataframe; if the column names aren't colors, remove color=df.columns

#source = "Publication"
student = form.text_input("Student name")
course = form.selectbox(
    "Choose course",
    ["Report Generation in Streamlit", "Advanced Cryptography"],
    index=0,
)
if course == "Advanced Cryptography":form.write ('Teste')

grade = form.slider("Grade", 1, 100, 60)
submit = form.form_submit_button("Generate PDF")

if submit:
    html = template.render(
        student=student,
        #course=course,
        metric=metric,
        grade=f"{grade}/100",
        date=date.today().strftime("%B %d, %Y"),
            )
    chart = chart
    
    #pdf = pdfkit.from_string(fig, 'test.pdf', options=opt)

    pdf = pdfkit.from_string(html, False)
    #pdf = pdfkit.from_string(chart, 'test.pdf')
    st.balloons()

    right.success("🎉 Your diploma was generated!")
    # st.write(html, unsafe_allow_html=True)
    # st.write("")
    right.download_button(
        "⬇️ Download PDF",
        data=pdf,
        file_name="diploma.pdf",
        mime="application/octet-stream",
        
    )
    
        

data = [go.Bar(x=[2, 4, 6], y=[10, 12, 15])]
layout = go.Layout(title='A Simple Plot', width=800, height=640)

fig = offline.plot({'data': data,
                    'layout': layout},
                    auto_open=False,
                    show_link=False,
                    output_type='div', include_plotlyjs=True)

opt = {'javascript-delay': 1000,
       'no-stop-slow-scripts': None,
       'debug-javascript': None}

pdfkit.from_string(fig, 'test.pdf', options=opt)
  
