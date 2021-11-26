import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe

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
source = "Publication"
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
        metric=source,
        grade=f"{grade}/100",
        date=date.today().strftime("%B %d, %Y"),
            )

    pdf = pdfkit.from_string(html, False)
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

    chart_data=pd.DataFrame({"source_number":[11199,11328,11287,32345,12342,1232,13456,123244,1235],
    "location":["loc1","loc2","loc3","loc1","loc1","loc2","loc3","loc2","loc1"],
    "category":["cat1","cat3","cat1","cat3","cat2","cat3","cat2","cat3","cat1"],
    })
    

st.bar_chart(chart_data)
