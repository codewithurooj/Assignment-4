import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }
    .stApp {
        background-color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    st.write("File uploaded...")
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.write("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select X-axis column", columns)
    y_column = st.selectbox("Select Y-axis column", columns)

    

if st.button("Generate Plot"):
    fig, ax = plt.subplots()
    filtered_df.plot(x=x_column, y=y_column, ax=ax)
    st.pyplot(fig)


else:
    st.write("Waiting on file upload...")
