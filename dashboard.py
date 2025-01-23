import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load the dataset
df = pd.read_csv('Enhanced_Cleaned_updated_combined_data.csv')

# Streamlit layout
st.title("Streamlit Dashboard for Dataset Insights")
st.sidebar.header("Data Exploration")

# Show basic information and summary statistics
st.sidebar.subheader("Basic Information")
st.sidebar.write("Dataset shape: ", df.shape)
st.sidebar.write("Dataset columns: ", df.columns)
st.sidebar.write("Dataset types: ", df.dtypes)

st.sidebar.subheader("Summary Statistics")
st.sidebar.write(df.describe())

# Show data preview
st.subheader("Data Preview")
st.write(df.head())

# Select only numeric columns for correlation analysis
numeric_df = df.select_dtypes(include=[float, int])

# Calculate the correlation matrix and plot heatmap
st.subheader("Correlation Heatmap")
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
st.pyplot()

# Create interactive filters for better exploration
st.sidebar.subheader("Filters")

# Create a filter for Performance Category
performance_category = st.sidebar.selectbox("Select Performance Category", df['Performance Category'].unique())
filtered_data = df[df['Performance Category'] == performance_category]

# Display filtered data
st.subheader(f"Filtered Data for {performance_category} Performance Category")
st.write(filtered_data)

# Create a bar plot for numeric data based on performance category
st.subheader("Performance Analysis")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=filtered_data, x='Performance Category', y='Overall Performance', ax=ax)
st.pyplot()

# Optional: Include AI-generated insights (example placeholder)
st.subheader("AI-Generated Insights")
st.write("""
    The dataset indicates a strong correlation between sleep time and overall performance. 
    Students who sleep longer tend to have better academic performance. Additionally, 
    parental involvement in education also seems to play a significant role in enhancing performance.
""")