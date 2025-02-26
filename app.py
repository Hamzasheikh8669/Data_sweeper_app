import streamlit as st
import pandas as pd

# Title of the app
st.title("Data Sweeper App")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Display the original data
    st.subheader("Original Data")
    st.write(df)

    # Option to remove duplicates
    if st.checkbox("Remove Duplicates"):
        df = df.drop_duplicates()
        st.success("Duplicates removed!")

    # Option to handle missing values
    if st.checkbox("Handle Missing Values"):
        missing_option = st.selectbox("Select an option", ["Drop Rows", "Fill with Mean", "Fill with Median"])
        if missing_option == "Drop Rows":
            df = df.dropna()
            st.success("Rows with missing values dropped!")
        elif missing_option == "Fill with Mean":
            df.fillna(df.mean(), inplace=True)
            st.success("Missing values filled with mean!")
        elif missing_option == "Fill with Median":
            df.fillna(df.median(), inplace=True)
            st.success("Missing values filled with median!")

    # Display the cleaned data
    st.subheader("Cleaned Data")
    st.write(df)

    # Option to download the cleaned data
    csv = df.to_csv(index=False)
    st.download_button("Download Cleaned Data", csv, "cleaned_data.csv", "text/csv")
