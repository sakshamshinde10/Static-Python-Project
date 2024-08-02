import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
df = pd.read_csv('weather_data.csv')
# Streamlit app
st.title('EDA of climate Analysis')

# Printing the DataFrame
st.subheader('Original dataset')
st.write(df)
st.write(df.shape) 
# Printing the Update Dataframe
# Null values
st.subheader("After handling missing values")


st.write(df)
st.write(df.shape)

# Duplicates
st.subheader("After handling duplicates")
df.drop_duplicates(inplace=True)
st.write(df)
st.write(df.shape)

# Example of EDA with Streamlit
st.subheader('Bar Chart Example')
x_column = st.selectbox('Select X-axis column', df.columns,index=2)
# y_column = st.selectbox('Select Y-axis column', df.columns)

# Ensure x and y columns are different
if x_column == 0:
    st.error('Please select different columns for X and Y axes.')
else:
    # Bar chart
    st.subheader('Bar Chart')
    st.bar_chart(df[x_column].head(10),color='#ff69b4')

    # Line chart
    st.subheader('Line Chart')
    st.line_chart(df[x_column].head(60))

    # Scatter plot
    st.subheader('Scatter Plot')
    st.scatter_chart(df[x_column].head(60))

    # area chart
    st.area_chart(df[x_column].head(60))

    # pie chart using matplotlib
    st.subheader("Pie chart using matplotlib")
    plt.figure(figsize=[50,50])
    plt.pie(df['Temperature_C'].head(60).value_counts().values,autopct='%1.1f%%',labels=df['Temperature_C'].head(60).value_counts().index, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
    st.pyplot(plt)


    st.pyplot(plt)










