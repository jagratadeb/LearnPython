import streamlit as st
import pandas as pd

st.title("Streamlit Test Input")

name = st.text_input("Enter your name:")

age = st.slider("Select you age:",0,100,25)
st.write(f"Your age is {age}")

options = ["Python","Java","C++","JavaScript"]
choice = st.selectbox("Choose your favourite language:", options)
st.write(f"You selected {choice}")

data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [28, 24, 22],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
st.write("User Data:")
st.write(df)

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    uploaded_df = pd.read_csv(uploaded_file)
    st.write("Uploaded CSV Data:")
    st.write(uploaded_df)

if name:
    st.write(f"Hello, {name}")

# For more details, visit: https://docs.streamlit.io/