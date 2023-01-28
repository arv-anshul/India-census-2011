""" A rough analysis like the CampusX done in his project. """

import plotly.express as px
import streamlit as st
from pandas import read_csv

# Page config
st.set_page_config('Rough Analysis', '', 'wide')

# --- Import Dateset ---
district = read_csv('data/District_census_2011.csv')
district.drop(columns=['Male', 'Female', 'Literate', 'Male_Literate', 'Female_Literate'],
              inplace=True)

state = read_csv('data/State_census_2011.csv')

# --- Sidebar ---
st.sidebar.title('Census 2011 Dashboard')

ind_states = list(district['State'].unique())
ind_states.insert(0, 'All States')
sl_state = st.sidebar.selectbox('Select State', ind_states)

use_cols = district.columns[4:]
primary = st.sidebar.selectbox('Select primary data', use_cols)
secondary = st.sidebar.selectbox('Select secondary data', use_cols)

# --- --- --- --- --- --- --- --- --- --- #
if st.sidebar.button('Plot'):
    if sl_state != 'All States':
        df = district.query('State==@sl_state')
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', size=primary, color=secondary,
                                zoom=3, mapbox_style='carto-positron',
                                title=f'{primary} VS {secondary}'.title(), hover_name='District')
        st.plotly_chart(fig, True)
    else:
        fig = px.scatter_mapbox(state, lat='Latitude', lon='Longitude', size=primary, color=secondary,
                                zoom=3, mapbox_style='carto-positron',
                                title=f'{primary} VS {secondary}'.title(), hover_name='State')
        st.plotly_chart(fig, True)
