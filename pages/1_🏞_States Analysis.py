""" India 2011 census dashboard with streamlit and python. """

import plotly.express as px
import streamlit as st
from pandas import read_csv

# --- --- Import datasets --- ---
state_df = read_csv('../data/State_census_2011.csv')

# Page config
st.set_page_config('State Analysis', '🏞', 'wide')

# --- --- Sidebar --- ---
st.sidebar.title('Cenuse 2011')
choice_menu = ['Population', 'Household Numbers', 'Household Size',
               'Religion', 'Caste (SC & ST)', 'Literacy', 'Education', 'Age Groups']
choice = st.sidebar.selectbox('Choose analysis', choice_menu)


if choice == 'Population':
    st.title('India Population Analysis')

    st.subheader(f'Population distributed over all Indian States.')
    px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude',
                      size='Population', color='State',
                      hover_name='District', zoom=3,
                      mapbox_style='open-street-map',
                      title='Shows the Population of Indian States.')
