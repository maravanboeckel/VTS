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
         st.title('Kaart')
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
        
         def add_categorical_legend(folium_map, title, colors, labels):
                  if len(colors) != len(labels):
                  raise ValueError("colors and labels must have the same length.")

                  color_by_label = dict(zip(labels, colors))
    
                  legend_categories = ""     
                  for label, color in color_by_label.items():
                  legend_categories += f"<li><span style='background:{color}'></span>{label}</li>"
        
                  legend_html = f"""
                  <div id='maplegend' class='maplegend'>
                  <div class='legend-title'>{title}</div>
                  <div class='legend-scale'>
                  <ul class='legend-labels'>
                  {legend_categories}
                  </ul>
                  </div>
                  </div>
                  """
                  script = f"""
                  <script type="text/javascript">
                  var oneTimeExecution = (function() {{
                                    var executed = false;
                                    return function() {{
                                    if (!executed) {{
                                             var checkExist = setInterval(function() {{
                                                      if ((document.getElementsByClassName('leaflet-top leaflet-right').length) || (!executed)) {{
                                                      document.getElementsByClassName('leaflet-top leaflet-right')[0].style.display = "flex"
                                                      document.getElementsByClassName('leaflet-top leaflet-right')[0].style.flexDirection = "column"
                                                      document.getElementsByClassName('leaflet-top leaflet-right')[0].innerHTML += `{legend_html}`;
                                                      clearInterval(checkExist);
                                                      executed = true;
                                                      }}
                                                      }}, 100);
                                    }}
                                    }};
                           }})();
                  oneTimeExecution()
                  </script>
                  """
   

                  css = """

                  <style type='text/css'>
                  .maplegend {
                  z-index:9999;
                  float:right;
                  background-color: rgba(255, 255, 255, 1);
                  border-radius: 5px;
                  border: 2px solid #bbb;
                  padding: 10px;
                  font-size:12px;
                  positon: relative;
                  }
                  .maplegend .legend-title {
                  text-align: left;
                  margin-bottom: 5px;
                  font-weight: bold;
                  font-size: 90%;
                  }
                  .maplegend .legend-scale ul {
                  margin: 0;
                  margin-bottom: 5px;
                  padding: 0;
                  float: left;
                  list-style: none;
                  }
                  .maplegend .legend-scale ul li {
                  font-size: 80%;
                  list-style: none;
                  margin-left: 0;
                  line-height: 18px;
                  margin-bottom: 2px;
                  }
                  .maplegend ul.legend-labels li span {
                  display: block;
                  float: left;
                  height: 16px;
                  width: 30px;
                  margin-right: 5px;
                  margin-left: 0;
                  border: 0px solid #ccc;
                  }
                  .maplegend .legend-source {
                  font-size: 80%;
                  color: #777;
                  clear: both;
                  }
                  .maplegend a {
                  color: #777;
                  }
                  </style>
                  """

                  folium_map.get_root().header.add_child(folium.Element(script + css))

                  return folium_map
