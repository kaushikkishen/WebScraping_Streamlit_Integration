#!/usr/bin/env python
# coding: utf-8

# In[1]:


import psycopg2
import pandas as pd


# In[2]:


def get_data_from_postgres(query):
    # Set up the connection details
    conn = psycopg2.connect(
        host="localhost",
        database="red_bus_details",
        user="postgres",
        password="admin",
        port=5432
    )
    
    # Execute the query and fetch data into a pandas DataFrame
    df = pd.read_sql_query(query, conn)
    
    # Close the connection
    conn.close()
    
    return df


# In[9]:


# !pip install streamlit
# !pip uninstall protobuf
# !pip install protobuf==3.20.*


# In[10]:


import streamlit as st


# In[12]:


# Function to load data from PostgreSQL
def load_data():
    query = "SELECT * FROM bus_details;"  # Example query
    data = get_data_from_postgres(query)
    return data


# In[15]:


df = load_data()


# In[16]:


df.head()


# In[17]:


# Streamlit app code
def app():
    st.title("Bus Details Data Analysis")

    # Load data from PostgreSQL
    df = load_data()

    # Show the data in a table before filtering
    st.subheader("Raw Data")
    st.write(df)

    # Add filter options using Streamlit widgets
    st.sidebar.subheader("Filter Options")

    # Bus type filter
    bus_types = st.sidebar.multiselect("Select Bus Type", df['bus_type'].unique())
    if bus_types:
        df = df[df['bus_type'].isin(bus_types)]
    
    # Price range filter
    min_price, max_price = st.sidebar.slider("Select Price Range", float(df['price'].min()), float(df['price'].max()), (float(df['price'].min()), float(df['price'].max())))
    df = df[(df['price'] >= min_price) & (df['price'] <= max_price)]

    # Start Time filter
    start_time = st.sidebar.selectbox("Select Start Time", df['start_time'].unique())
    if start_time:
        df = df[df['start_time'] == start_time]

    # Show the filtered data
    st.subheader("Filtered Data")
    st.write(df)

    # Show some statistics based on the filtered data
    st.subheader("Statistics")
    st.write(df.describe())


# In[18]:


if __name__ == "__main__":
    app()


# In[ ]:




