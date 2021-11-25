#import streamlit as st
#from fpdf import FPDF
#import base64
#from pathlib import Path

#report_text = st.text_input("Report Text")

#st.code("WOW", language='python')

#def read_markdown_file(markdown_file):
#    return Path(markdown_file).read_text()

#intro_markdown = read_markdown_file("introduction.md")
#st.markdown(intro_markdown, unsafe_allow_html=True)

import streamlit as st
from fpdf import FPDF
import base64

report_text = st.text_input("Report Text")


export_as_pdf = st.button("Export Report")

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

if export_as_pdf:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, report_text)
    
    html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")

    st.markdown(html, unsafe_allow_html=True)
