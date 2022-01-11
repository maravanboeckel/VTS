#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
import folium
import streamlit as st
from streamlit_folium import folium_static
import plotly.express as px




         

# In[ ]:

st.title('Kaart met scheefstand lantaarnpalen in Houten')

vergelijk1=pd.read_csv('Data_kaart.csv')
st.set_page_config(layout="wide")
#rad = st.sidebar.radio(options=('Grafiek','Kaart'),label='Selecteer')
st.sidebar.subheader('Gemaakt door:')
st.sidebar.write('Mara van Boeckel')
st.sidebar.write('Lisa Mulder')
st.sidebar.write('Rhode Rebel')

st.sidebar.markdown('#')
st.sidebar.markdown('#')

# In[ ]:
#if rad == 'Grafiek':
fig = px.line(vergelijk1, x="lantaarnpaal_nummer", y=["scheefstand","scheefstand_tov_kader"],labels={
      "value": "Scheefstand (graden)", 'variable':''},
       title='Scheefstand waterpas en algoritme')


st_plotly_chart(fig)

#In[ ]:
#if rad == 'Kaart':
         
