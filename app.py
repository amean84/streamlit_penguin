import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

@st.cache
def load_data():
    df = sns.load_dataset('penguins')
    df.columns = [column.replace(" ", "_").lower() for column in df.columns]
    df = df.dropna(how='any')
    return df

df = load_data()
#df = sns.load_dataset('penguins')
#df.columns = [column.replace(" ", "_").lower() for column in df.columns]
#df = df.dropna(how='any')

st.title('🐧 Penguin Data Exploration App 🐧')
st.markdown('This is demo app to explore data.')

st.write('A dataset has already been loaded for you. These are the available data fields:')
st.write('Categorical Variables',list(df.select_dtypes(include='object')))
st.write('Numerical Variables',list(df.select_dtypes(include='number')))
if st.checkbox('Click to view sample of dataframe (First 10 Rows)'):
    st.write(df.head(10))

sns.set_palette('terrain')

st.subheader('Barchart')
bar_objects = df.select_dtypes(include='object')
bar_count = st.selectbox('I want to count penguins by:', bar_objects.columns, key=1)
sns.countplot(x=bar_count, data=df)
plt.title('Penguin Count')
st.pyplot()

st.subheader('Violin Plot')
if st.checkbox('Click to view Violin Plot', key=2):
    violin_cat_objects = df.select_dtypes(include='object')
    violin0 = st.selectbox('Which variable on X-Axis?',violin_cat_objects.columns)
    violin_objects = df.select_dtypes(include='number')
    violin1 = st.selectbox('Which variable on Y-Axis?',violin_objects.columns)
    sns.violinplot(x=violin0, y=violin1, data=df)
    plt.title('Distribution by Species')
    st.pyplot()

st.subheader('Scatterplot')
if st.checkbox('Click to view Scatterplot', key=3):
    scatter_objects = df.select_dtypes(include='number')
    col1 = st.selectbox('Which variable on X-Axis?',scatter_objects.columns)
    col2 = st.selectbox('Which variable on Y-Axis?',scatter_objects.columns)
    col_group = st.selectbox('Color by:', bar_objects.columns)
    sns.scatterplot(x=col1, y=col2,hue=col_group, data=df)
    plt.title('Penguin Scatterplot')
    st.pyplot()

st.subheader('Build Your Own Relational Plot')
if st.checkbox('Click to view Relational Plot', key=4):
    cat_options=['species','island','sex']
    plot_options=['scatter','line']
    plot_kind = st.selectbox('Plot Kind:', options=plot_options)
    facet_col = st.selectbox('Facet Column:', options=cat_options)
    facet_row = st.selectbox('Facet Row:', options=cat_options)
    color_by = st.selectbox('Color By:', options=cat_options)
    sns.relplot(x='bill_length_mm', y='flipper_length_mm', kind=plot_kind, hue=color_by, col=facet_col, row=facet_row, data=df)
    st.pyplot()

st.subheader('Pairplot')
if st.checkbox('Click to view Pairplot of Numerical Features', key=5):
    sns.pairplot(df, hue='species', markers=["o", "s", "D"])
    st.pyplot()
    
