#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
import folium
import streamlit as st
from streamlit_folium import folium_static
import plotly.express as px




         

# In[ ]:

#

vergelijk1=pd.read_csv('Data_kaart.csv')
st.set_page_config(layout="wide")
rad = st.sidebar.radio(options=('Grafiek','Kaart'),label='Selecteer')
st.sidebar.subheader('Gemaakt door:')
st.sidebar.write('Mara van Boeckel')
st.sidebar.write('Lisa Mulder')
st.sidebar.write('Rhode Rebel')

st.sidebar.markdown('#')
st.sidebar.markdown('#')

# In[ ]:
if rad == 'Grafiek':
         st.title('Grafiek')
# fig = px.line(vergelijk1, x="lantaarnpaal_nummer", y=["scheefstand","scheefstand_tov_kader"],labels={
#       "value": "Scheefstand (graden)", 'variable':''},
#        title='Scheefstand waterpas en algoritme')
# st_plotly_chart(fig)

#In[ ]:
if rad == 'Kaart':
         def scheef(scheefstand):
                  if  abs(scheefstand) >= 1 and scheefstand <3:
                           color = 'orange'
                           return color
                  elif abs(scheefstand) >= 3 and scheefstand < 6:
                           color='red'
                           return color
                  elif abs(scheefstand) >=6:
                           color = 'darkred'
                           return color
                  else:
                           color = 'green'
                           return color
                  
         def scheef1(scheefstand_tov_kader):
                  if  abs(scheefstand_tov_kader) >= 1 and scheefstand_tov_kader <3:
                           color = 'orange'
                           return color
                  elif abs(scheefstand_tov_kader) >= 3 and scheefstand_tov_kader < 6:
                           color='red'
                           return color
                  elif abs(scheefstand_tov_kader) >=6:
                           color = 'darkred'
                           return color
                  else:
                           color = 'green'
                           return color  
