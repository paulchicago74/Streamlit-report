import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import io

# Load the data
@st.experimental_memo
def load_data():
    return pd.DataFrame(
        {
            "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
            "Contestant": ["Alex", "Alex", "Alex", "Jordan", "Jordan", "Jordan"],
            "Number Eaten": [2, 1, 3, 1, 3, 2],
        }
    )

# Create and cache a Plotly figure
@st.experimental_memo
def create_figure(df):
    fig = go.Figure()
    for contestant, group in df.groupby("Contestant"):
        fig.add_trace(
            go.Bar(
                x=group["Fruit"],
                y=group["Number Eaten"],
                name=contestant,
                hovertemplate="Contestant=%s<br>Fruit=%%{x}<br>Number Eaten=%%{y}<extra></extra>"
                % contestant,
            )
        )
    fig.update_layout(legend_title_text="Contestant")
    fig.update_xaxes(title_text="Fruit")
    fig.update_yaxes(title_text="Number Eaten")
    return fig

df = load_data()
fig = create_figure(df)

# Create an in-memory buffer
buffer = io.BytesIO()

# Save the figure as a pdf to the buffer
fig.write_image(file=buffer, format="pdf")

# Download the pdf from the buffer
st.download_button(
    label="Download PDF",
    data=buffer,
    file_name="figure.pdf",
    mime="application/pdf",
)

st.plotly_chart(fig)



           
        


