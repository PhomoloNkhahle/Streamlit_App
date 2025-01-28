import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
data = pd.read_csv('Cleaned_combined_data.csv', encoding='utf-8')
st.title("Interactive Data Dashboard")
st.write("This app visualizes key insights from the dataset.")
# Convert categorical columns to numeric while preserving original labels for visualization
categorical_cols = data.select_dtypes(include=['object']).columns
label_encoders = {}

for col in categorical_cols:
    if col not in ['Name', 'Parents Name', 'Parental Involvement Insights']:
        le = LabelEncoder()
        data[f"{col}_encoded"] = le.fit_transform(data[col].astype(str))
        label_encoders[col] = le

# Show summary statistics
st.header("Summary Statistics")
st.write(data.describe())

# Correlation matrix
st.header("Correlation Heatmap")
corr_matrix = data.select_dtypes(include=[np.number]).corr()
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Visualizations
st.header("Visualizations")

# Distribution of Overall Performance
st.subheader("Distribution of Overall Performance")
fig, ax = plt.subplots()
sns.histplot(data["Overall Performance"], kde=True, ax=ax, color='blue')
st.pyplot(fig)

# Performance by Parent Education Level
st.subheader("Performance by Parent Education Level")
fig, ax = plt.subplots()
sns.boxplot(x="Parent Education Level", y="Overall Performance", data=data, ax=ax)
st.pyplot(fig)

# Scatter plot for normalized scores
st.subheader("Scatter Plot: Normalized Maths vs Normalized Reading")
fig, ax = plt.subplots()
sns.scatterplot(x="Normalized Maths", y="Normalized Reading", hue="Performance Category", data=data, ax=ax)
st.pyplot(fig)

# Interactive filters
st.sidebar.header("Filters")
selected_gender = st.sidebar.selectbox("Gender", options=data["Gender"].dropna().unique())
filtered_data = data[data["Gender"] == selected_gender]

st.subheader("Filtered Data")
st.write(filtered_data)

# Insights
st.header("Key Insights")
st.write("""
- **Correlation Analysis:** There is a strong positive correlation between normalized math, reading, and writing scores.
- **Parental Education:** Higher parental education levels are generally associated with better overall performance.
- **Sleep Impact:** Students with optimal sleep tend to perform better than those with insufficient sleep.
- **Social Media:** Excessive social media use negatively impacts performance.
""")