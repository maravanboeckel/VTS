# #!/usr/bin/env python
# # coding: utf-8

import pandas as pd
import folium
import streamlit as st
from streamlit_folium import folium_static
import plotly.express as px
from PIL import Image

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 200px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 200px;
        margin-left: -200px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

rad = st.sidebar.radio(options=('Home','Grafiek','Distributie','Spreidingsdiagram','Kaart'),label='Selecteer')
st.sidebar.markdown('#')
st.sidebar.markdown('#')
st.sidebar.markdown('#')
st.sidebar.markdown('#')
st.sidebar.markdown('#')
st.sidebar.markdown('#')
st.sidebar.markdown('#')
st.sidebar.markdown('#')
st.sidebar.subheader('Gemaakt door:')
st.sidebar.write('Mara van Boeckel')
st.sidebar.write('Lisa Mulder')
st.sidebar.write('Rhodé Rebel')

Houten=pd.read_csv('Houten.csv')
if rad == 'Home':
    st.header('Project voor Velo Tech Solutions')
    st.header('De scheefstand bepalen van lantaarnpalen met een algoritme')
    imghome = Image.open("HOUTEN69.jpg")
    st.image(imghome, width=450)


if rad == 'Grafiek':
    st.header('Grafieken van de scheefstand per lantaarnpaal gemeten met de elektronische waterpas en het algoritme')
    'Als er een - staat voor de scheefstand betekent dat de lantaarnpaal naar rechts scheef staat. Bij positief getal is de lantaarnpaal scheef naar links'
    'Als correctie wordt de gemiddelde fout van 0,84⁰ van de scheefstand van het algoritme afgehaald.'
    'Het is mogelijk om de grafieken in te zoomen.'
    st.markdown('#')
    
#     col_1, col_1a, col2 = st.columns([3,0.3,3])
#     with col_1:
#         st.markdown("<h4 style='text-align: center;'>Voor de correctie</h4>", unsafe_allow_html=True)
        
#         fig = px.line(Houten, x="lantaarnpaal_nummer", y=["scheefstand","scheefstand_tov_kader"],
#               labels={"value": "Scheefstand (graden)", 'variable':'','lantaarnpaal_nummer':'Lantaarnpaal'}, 
#               color_discrete_map={'scheefstand': '#4160ad','scheefstand_tov_kader': '#d1534f'})
#         fig.update_layout(plot_bgcolor='#f0f1f1')

#         newnames = {'scheefstand':'Scheefstand elektronische waterpas', 'scheefstand_tov_kader': 'Scheefstand algoritme'}
#         fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
#                                       legendgroup = newnames[t.name],
#                                       hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])))

#         st.plotly_chart(fig,use_column_width=True)
        
#     with col_1a:
#         st.markdown('')
        
#     with col_2:
#         st.markdown("<h4 style='text-align: center;'>Na de correctie</h4>", unsafe_allow_html=True)
#         fig5 = px.line(Houten, x="lantaarnpaal_nummer", y=["scheefstand","AL_na_corr"],
#         labels={"value": "Scheefstand (graden)", 'variable':'','lantaarnpaal_nummer':'Lantaarnpaal'},
#         color_discrete_map={'scheefstand': '#4160ad','AL_na_corr': '#d1534f'},
#         hover_name="lantaarnpaal_nummer")
#         fig5.update_layout(plot_bgcolor='#f0f1f1')

#         newnames3 = {'scheefstand':'Scheefstand elektronische waterpas', 'AL_na_corr': 'Scheefstand algoritme na correctie'}
#         fig5.for_each_trace(lambda t: t.update(name = newnames3[t.name],
#                                   legendgroup = newnames3[t.name],
#                                   hovertemplate = t.hovertemplate.replace(t.name, newnames3[t.name])))
#         st.plotly_chart(fig5,use_column_width=True)
        
    col_1, col_2 = st.columns(2)
    with col_1:
        st.markdown("<h4 style='text-align: center;'>Voor de correctie</h4>", unsafe_allow_html=True)
        
        fig = px.line(Houten, x="lantaarnpaal_nummer", y=["scheefstand","scheefstand_tov_kader"],
              labels={"value": "Scheefstand (graden)", 'variable':'','lantaarnpaal_nummer':'Lantaarnpaal'}, 
              color_discrete_map={'scheefstand': '#4160ad','scheefstand_tov_kader': '#d1534f'})
        fig.update_layout(title_x=0.8,plot_bgcolor='#f0f1f1')

        newnames = {'scheefstand':'Scheefstand elektronische waterpas', 'scheefstand_tov_kader': 'Scheefstand algoritme'}
        fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])))

        st.plotly_chart(fig,use_column_width=True)
    
    with col_2:
        st.markdown("<h4 style='text-align: center;'>Na de correctie</h4>", unsafe_allow_html=True)

        fig5 = px.line(Houten, x="lantaarnpaal_nummer", y=["scheefstand","AL_na_corr"],
        labels={"value": "Scheefstand (graden)", 'variable':'','lantaarnpaal_nummer':'Lantaarnpaal'},
        color_discrete_map={'scheefstand': '#4160ad','AL_na_corr': '#d1534f'},
        hover_name="lantaarnpaal_nummer")
        fig5.update_layout(title_x=0.8,plot_bgcolor='#f0f1f1')

        newnames3 = {'scheefstand':'Scheefstand elektronische waterpas', 'AL_na_corr': 'Scheefstand algoritme na correctie'}
        fig5.for_each_trace(lambda t: t.update(name = newnames3[t.name],
                                  legendgroup = newnames3[t.name],
                                  hovertemplate = t.hovertemplate.replace(t.name, newnames3[t.name])))
        st.plotly_chart(fig5,use_column_width=True)
                
if rad == 'Distributie':
    st.header('Distributie van de absolute scheefstanden')
    'Het is mogelijk om het historgram in te zoomen.'
    col_2, col_3, col_4 = st.columns([3,0.3,3])
    with col_2:
        st.markdown("<h4 style='text-align: center;'>Voor de correctie</h4>", unsafe_allow_html=True)
        fig1=px.histogram(Houten, x=["scheefstand_abs","scheefstand_tov_kader_abs"],
                  nbins=17, labels={'value':'Scheefstand absoluut (graden)', 'variable':''},
                  color_discrete_map={'scheefstand_abs': '#4160ad','scheefstand_tov_kader_abs': '#d1534f'})
        fig1.update_layout(barmode='group',yaxis_title_text='Frequentie',plot_bgcolor='#f0f1f1')
        fig1.update_xaxes(dtick=1)

        newnames2 = {'scheefstand_abs':'Scheefstand elektronische waterpas', 'scheefstand_tov_kader_abs': 'Scheefstand algoritme'}
        fig1.for_each_trace(lambda t: t.update(name = newnames2[t.name],
                                       legendgroup = newnames2[t.name],
                                       hovertemplate = t.hovertemplate.replace(t.name, newnames2[t.name])))
        st.plotly_chart(fig1,use_column_width=True)
        
    with col_3:
        st.markdown('')
    with col_4:
        st.markdown("<h4 style='text-align: center;'>Na de correctie</h4>", unsafe_allow_html=True)

        fig6=px.histogram(Houten, x=["scheefstand_abs","AL_na_corr_abs"],
                                  nbins=17, labels={'value':'Scheefstand absoluut (graden)', 'variable':''},
                                color_discrete_map={'scheefstand_abs': '#4160ad','AL_na_corr_abs': '#d1534f'})
        fig6.update_layout(barmode='group',yaxis_title_text='Frequentie',plot_bgcolor='#f0f1f1')
        fig6.update_xaxes(dtick=1)
        newnames4 = {'scheefstand_abs':'Scheefstand elektronische waterpas', 'AL_na_corr_abs': 'Scheefstand algoritme na correctie'}
        fig6.for_each_trace(lambda t: t.update(name = newnames4[t.name],
                                       legendgroup = newnames4[t.name],
                                       hovertemplate = t.hovertemplate.replace(t.name, newnames4[t.name])))   
        st.plotly_chart(fig6,use_column_width=True)
        
            
            
            
#     col_3, col_4 = st.columns(2)
#     with col_3:
#         st.markdown("<h4 style='text-align: center;'>Voor de correctie</h4>", unsafe_allow_html=True)

#         fig1=px.histogram(Houten, x=["scheefstand_abs","scheefstand_tov_kader_abs"],
#                   nbins=17, labels={'value':'Scheefstand absoluut (graden)', 'variable':''},
#                   color_discrete_map={'scheefstand_abs': '#4160ad','scheefstand_tov_kader_abs': '#d1534f'})
#         fig1.update_layout(barmode='group',yaxis_title_text='Frequentie',plot_bgcolor='#f0f1f1')
#         fig1.update_xaxes(dtick=1)

#         newnames2 = {'scheefstand_abs':'Scheefstand elektronische waterpas', 'scheefstand_tov_kader_abs': 'Scheefstand algoritme'}
#         fig1.for_each_trace(lambda t: t.update(name = newnames2[t.name],
#                                        legendgroup = newnames2[t.name],
#                                        hovertemplate = t.hovertemplate.replace(t.name, newnames2[t.name])))
#         st.plotly_chart(fig1,use_column_width=True)
        
#     with col_4:
#         st.markdown("<h4 style='text-align: center;'>Na de correctie</h4>", unsafe_allow_html=True)

#         fig6=px.histogram(Houten, x=["scheefstand_abs","AL_na_corr_abs"],
#                                   nbins=17, labels={'value':'Scheefstand absoluut (graden)', 'variable':''},
#                                 color_discrete_map={'scheefstand_abs': '#4160ad','AL_na_corr_abs': '#d1534f'})
#         fig6.update_layout(barmode='group',yaxis_title_text='Frequentie',plot_bgcolor='#f0f1f1')
#         fig6.update_xaxes(dtick=1)
#         newnames4 = {'scheefstand_abs':'Scheefstand elektronische waterpas', 'AL_na_corr_abs': 'Scheefstand algoritme na correctie'}
#         fig6.for_each_trace(lambda t: t.update(name = newnames4[t.name],
#                                        legendgroup = newnames4[t.name],
#                                        hovertemplate = t.hovertemplate.replace(t.name, newnames4[t.name])))   
#         st.plotly_chart(fig6,use_column_width=True)
        
        
if rad == 'Spreidingsdiagram':
    st.header('De scheefstand van de elektronische waterpas uitgezet tegen de scheefstand van het algoritme (per lantaarnpaal)')
    'De blauwe lijn die te zien is in de plot geeft de lijn 
    st.latex(y=x)
    'weer. Dit is de lijn die ontstaat als de scheefstand van de elektronische waterpas altijd gelijk is aan het algoritme. De oranje punten zijn de waargenomen scheefstanden.'
    'Het is mogelijk om de plot in te zoomen voor een plot zonder uitschieter.'
    col_5, col_6, col_7 = st.columns([3,0.3,3])
    with col_5:
        st.markdown("<h4 style='text-align: center;'>Voor de correctie</h4>", unsafe_allow_html=True)
    
        fig2=px.scatter(Houten,x='scheefstand',y='scheefstand_tov_kader',
                labels={'scheefstand':'Scheefstand elektronische waterpas (graden)',
                        'scheefstand_tov_kader':'Scheefstand algoritme (graden)'},
                color_discrete_sequence=['#d1534f'])
        fig2.add_shape(type='line', x0=-7, y0=-7, x1=18, y1=18, line=dict(color='#4160ad'))
        fig2.update_layout(plot_bgcolor='#f0f1f1')
        st.plotly_chart(fig2,use_column_width=True)
      
    with col_6:
        st.markdown('')
    with col_7:
        st.markdown("<h4 style='text-align: center;'>Na de correctie</h4>", unsafe_allow_html=True)
        fig7 = px.scatter(Houten,x='scheefstand',y='AL_na_corr',
                 labels={'scheefstand':'Scheefstand elektronische waterpas (graden)',
                         'AL_na_corr':'Scheefstand algoritme (graden)'},
                 color_discrete_sequence=['#d1534f'],
                 hover_name="lantaarnpaal_nummer")
        fig7.add_shape(type='line', x0=-7, y0=-7, x1=18, y1=18, line=dict(color='#4160ad'))
        fig7.update_layout(plot_bgcolor='#f0f1f1')
        st.plotly_chart(fig7,use_column_width=True)
        
    
#     col_5, col_6 = st.columns(2)
#     with col_5:
#         st.markdown("<h4 style='text-align: center;'>Voor de correctie</h4>", unsafe_allow_html=True)
    
#         fig2=px.scatter(Houten,x='scheefstand',y='scheefstand_tov_kader',
#                 labels={'scheefstand':'Scheefstand elektronische waterpas (graden)',
#                         'scheefstand_tov_kader':'Scheefstand algoritme (graden)'},
#                 color_discrete_sequence=['#d1534f'])
#         fig2.add_shape(type='line', x0=-7, y0=-7, x1=18, y1=18, line=dict(color='#4160ad'))
#         fig2.update_layout(plot_bgcolor='#f0f1f1')
#         st.plotly_chart(fig2,use_column_width=True)
        
#     with col_6:
#         st.markdown("<h4 style='text-align: center;'>Na de correctie</h4>", unsafe_allow_html=True)
    
#         fig7 = px.scatter(Houten,x='scheefstand',y='AL_na_corr',
#                  labels={'scheefstand':'Scheefstand elektronische waterpas (graden)',
#                          'AL_na_corr':'Scheefstand algoritme (graden)'},
#                  color_discrete_sequence=['#d1534f'],
#                  hover_name="lantaarnpaal_nummer")
#         fig7.add_shape(type='line', x0=-7, y0=-7, x1=18, y1=18, line=dict(color='#4160ad'))
#         fig7.update_layout(plot_bgcolor='#f0f1f1')
#         st.plotly_chart(fig7,use_column_width=True)


if rad == 'Kaart':
    st.header('Kaart van (scheve) lantaarnpalen in Houten')
    'Het is mogelijk de kaarten in te zoomen. Als je op een lantaarnpaal klikt komt de informatie van de lantaarnpaal zichtbaar.' 
    st.markdown('#')
    
    st.markdown("<h3 style='text-align: center;'>Voor de correctie</h3>", unsafe_allow_html=True)
 
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3 style='text-align: center;'>Elektronische waterpas</h3>", unsafe_allow_html=True)
    with col2:
        st.markdown("<h3 style='text-align: center;'>Algoritme</h3>", unsafe_allow_html=True)
        
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
        
    def scheef2(AL_na_corr):
        if  abs(AL_na_corr) >= 1 and AL_na_corr <3:
            color = 'orange'
            return color
        elif abs(AL_na_corr) >= 3 and AL_na_corr < 6:
            color='red'
            return color
        elif abs(AL_na_corr) >=6:
            color = 'darkred'
            return color
        else:
            color = 'green'
            return color

    # Toevoegen van een categorische legenda
    # (bron: https://stackoverflow.com/questions/65042654/how-to-add-categorical-legend-to-python-folium-map)

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

    map_houten= folium.plugins.DualMap(location=[52.015154,5.171879], zoom_start = 15)
    tooltip = "Klik voor informatie"

    waterpas= folium.FeatureGroup(name='Scheefstand elektronische waterpas',show=False)
    algoritme= folium.FeatureGroup(name='Scheefstand algoritme',show=True)


    for row in Houten.iterrows():
        row_values = row[1]
        location = [row_values['lat'], row_values['lon']]
        popup = ('Fotonummer:'+' '+ row_values['lantaarnpaal_nummer']+'<strong>'+'<br>'+'<br>'+
                 'Scheefstand: '+ str(round(row_values['scheefstand'],2))+'°'+'</strong>'+'<br>'+'<br>'+
                'Lat, lon: '+str(row_values['lat'])+',' + '<br>' + str(row_values['lon'])    )

        marker = folium.CircleMarker(location = location,popup=popup,tooltip=tooltip,color=scheef(row_values['scheefstand']), fill_color=scheef(row_values['scheefstand']))
        marker.add_to(waterpas)
        waterpas.add_to(map_houten.m1)


    for row in Houten.iterrows():
        row_values = row[1]
        location = [row_values['lat'], row_values['lon']]
        popup = ('Fotonummer:'+' '+ row_values['lantaarnpaal_nummer']+'<strong>'+'<br>'+'<br>'+
                 'Scheefstand: '+ str(round(row_values['scheefstand_tov_kader'],2))+'°'+'</strong>'+'<br>'+'<br>'+
                'Lat, lon: '+str(row_values['lat'])+',' + '<br>' + str(row_values['lon'])   )

        marker = folium.CircleMarker(location = location,popup=popup,tooltip=tooltip,color=scheef1(row_values['scheefstand_tov_kader']), fill_color=scheef1(row_values['scheefstand_tov_kader']))
        marker.add_to(algoritme)
        algoritme.add_to(map_houten.m2)

    #folium.LayerControl(position='topleft').add_to(map_houten)
    legend_houten = add_categorical_legend(map_houten, 'Scheefstand',
                               colors=['darkred','red', 'orange', 'green'],
                               labels=['Meer dan 6°', 'Tussen 3° en 6°', 'Tussen 1° en 3°', 'Minder dan 1°'])
    folium_static(map_houten, width = 1150, height = 750)
    
    st.markdown("<h3 style='text-align: center;'>Na de correctie</h3>", unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("<h3 style='text-align: center;'>Elektronische waterpas</h3>", unsafe_allow_html=True)
    with col4:
        st.markdown("<h3 style='text-align: center;'>Algoritme</h3>", unsafe_allow_html=True)
        
    map_houten1= folium.plugins.DualMap(location=[52.015154,5.171879], zoom_start = 15)
    tooltip = "Klik voor informatie"

    waterpas= folium.FeatureGroup(name='Scheefstand elektronische waterpas',show=False)
    algoritme= folium.FeatureGroup(name='Scheefstand algoritme',show=True)


    for row in Houten.iterrows():
        row_values = row[1]
        location = [row_values['lat'], row_values['lon']]
        popup = ('Fotonummer:'+' '+ row_values['lantaarnpaal_nummer']+'<strong>'+'<br>'+'<br>'+
                 'Scheefstand: '+ str(round(row_values['scheefstand'],2))+'°'+'</strong>'+'<br>'+'<br>'+
                'Lat, lon: '+str(row_values['lat'])+',' + '<br>' + str(row_values['lon'])    )

        marker = folium.CircleMarker(location = location,popup=popup,tooltip=tooltip,color=scheef(row_values['scheefstand']), fill_color=scheef(row_values['scheefstand']))
        marker.add_to(waterpas)
        waterpas.add_to(map_houten1.m1)


    for row in Houten.iterrows():
        row_values = row[1]
        location = [row_values['lat'], row_values['lon']]
        popup = ('Fotonummer:'+' '+ row_values['lantaarnpaal_nummer']+'<strong>'+'<br>'+'<br>'+
                 'Scheefstand: '+ str(round(row_values['AL_na_corr'],2))+'°'+'</strong>'+'<br>'+'<br>'+
                'Lat, lon: '+str(row_values['lat'])+',' + '<br>' + str(row_values['lon'])   )

        marker = folium.CircleMarker(location = location,popup=popup,tooltip=tooltip,color=scheef2(row_values['AL_na_corr']), fill_color=scheef2(row_values['AL_na_corr']))
        marker.add_to(algoritme)
        algoritme.add_to(map_houten1.m2)

    #folium.LayerControl(position='topleft').add_to(map_houten)
    legend_houten = add_categorical_legend(map_houten1, 'Scheefstand',
                               colors=['darkred','red', 'orange', 'green'],
                               labels=['Meer dan 6°', 'Tussen 3° en 6°', 'Tussen 1° en 3°', 'Minder dan 1°'])
    folium_static(map_houten1, width = 1150, height = 750)
