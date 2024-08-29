#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


def get_data():

    df = pd.read_csv('finalbusdetails.csv')
    
    return df


# In[9]:


# !pip install streamlit
# !pip uninstall protobuf
# !pip install protobuf==3.20.*


# In[1]:


import streamlit as st


# In[4]:


df = get_data()


# In[5]:


df.head()


# In[8]:


# Streamlit app code
def app():
    st.title("Bus Details Data Analysis")

    # Load data from PostgreSQL
    df = get_data()

    # Show the data in a table before filtering
    st.subheader("Raw Data")
    st.write(df)

    # Add filter options using Streamlit widgets
    st.sidebar.subheader("Filter Options")

    # Bus type filter
    bus_types = st.sidebar.multiselect("Select Bus Type", df['Bus_type'].unique())
    if bus_types:
        df = df[df['Bus_type'].isin(bus_types)]
    
    # Price range filter
    min_price, max_price = st.sidebar.slider("Select Price Range", float(df['Price'].min()), float(df['Price'].max()), (float(df['Price'].min()), float(df['Price'].max())))
    df = df[(df['Price'] >= min_price) & (df['Price'] <= max_price)]

    # Start Time filter
    start_time = st.sidebar.selectbox("Select Start Time", df['Start_time'].unique())
    if start_time:
        df = df[df['Start_time'] == start_time]

    # Show the filtered data
    st.subheader("Filtered Data")
    st.write(df)

    # Show some statistics based on the filtered data
    st.subheader("Statistics")
    st.write(df.describe())


# In[9]:


if __name__ == "__main__":
    app()


# In[ ]:




