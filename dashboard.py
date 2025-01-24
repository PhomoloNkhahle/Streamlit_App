import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the dataset
data = pd.read_csv('Cleaned_updated_combined_data.csv')

# Streamlit Markdown for Insights
st.title('Student Performance Dashboard')

st.markdown("""## Insights

This dashboard provides key insights into students' academic performance, parental involvement, and lifestyle factors. Use the interactive elements to explore the data in detail.

### Key Findings:
- **Performance Trends:** Analyze how parental education, test preparation, and sleep patterns influence academic performance.
- **Lifestyle Factors:** Examine the impact of social media and food habits on performance.
- **Correlations:** Identify relationships between different variables, such as normalized scores and overall performance.

""")

# Summary Statistics
st.subheader('Summary Statistics')
st.write(data.describe())

# Distribution of Overall Performance
st.subheader('Distribution of Overall Performance')
fig1, ax1 = plt.subplots()
sns.histplot(data['Overall Performance'], bins=20, kde=True, color='blue', ax=ax1)
ax1.set_title('Distribution of Overall Performance')
st.pyplot(fig1)

# Boxplot of Performance by Parent Education Level
st.subheader('Performance by Parent Education Level')
fig2, ax2 = plt.subplots()
sns.boxplot(x='Parent Education Level', y='Overall Performance', data=data, ax=ax2)
ax2.set_title('Overall Performance vs. Parent Education Level')
ax2.set_xlabel('Parent Education Level')
ax2.set_ylabel('Overall Performance')
st.pyplot(fig2)

# Correlation Heatmap
st.subheader('Correlation Heatmap')
fig3, ax3 = plt.subplots(figsize=(10, 8))
correlation = data.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f', ax=ax3)
ax3.set_title('Correlation Heatmap')
st.pyplot(fig3)

# Scatterplot: Normalized Maths vs. Normalized Reading
st.subheader('Normalized Maths vs. Normalized Reading')
fig4, ax4 = plt.subplots()
sns.scatterplot(x='Normalized Maths', y='Normalized Reading', hue='Performance Category', data=data, palette='viridis', ax=ax4)
ax4.set_title('Normalized Maths vs. Normalized Reading')
ax4.set_xlabel('Normalized Maths')
ax4.set_ylabel('Normalized Reading')
st.pyplot(fig4)

# Bar Chart: Sleep Category Distribution
st.subheader('Sleep Category Distribution')
fig5, ax5 = plt.subplots()
data['Sleep Category'].value_counts().plot(kind='bar', color='green', ax=ax5)
ax5.set_title('Sleep Category Distribution')
ax5.set_xlabel('Sleep Category')
ax5.set_ylabel('Count')
st.pyplot(fig5)

# Markdown for Additional Insights
st.markdown("""### Additional Insights
- **Correlation Heatmap:** Reveals strong positive/negative relationships between variables, aiding in understanding key performance drivers.
- **Parental Education Impact:** Boxplot analysis shows higher parental education is often associated with improved performance.
- **Sleep Patterns:** Bar chart highlights the distribution of sleep categories, reflecting lifestyle differences.
""")