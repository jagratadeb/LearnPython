import streamlit as st
import pandas as pd
import numpy as np

# Application title
st.title("Hello Streamlit")

# Display a simple text
st.write("This is a sentence")

# Dataframe
df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

st.write("Here is the dataframe")
st.write(df)

# Display a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a','b','c']
)
st.write(chart_data)
st.line_chart(chart_data)