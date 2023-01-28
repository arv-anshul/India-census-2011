""" India 2011 census dashboard with streamlit and python. """

import plotly.express as px
import streamlit as st
from pandas import read_csv
from utils.wide_to_long import wide_to_long

# Page config
st.set_page_config('State Analysis', '🏞', 'wide')

# --- Import datasets ---
state = read_csv('data/State_census_2011.csv')
(religion, household_number, caste,
 education, household_size, age_groups) = wide_to_long(state, 'State')

# --- Sidebar ---
st.sidebar.title('Cenuse 2011')
plot_type = st.sidebar.selectbox('Choose plot type',
                                 ['Maps', '2D Plots'])

if plot_type == 'Maps':
    choice_menu = ['Population', 'Sex Ratio', 'Literacy Rate',
                   'Male Literacy Rate', 'Female Literacy Rate']
    size = st.sidebar.selectbox('Choose size', choice_menu)
    color = st.sidebar.selectbox('Choose color', choice_menu)
    # --- --- --- --- --- --- --- --- --- --- #
    fig = px.scatter_mapbox(state, lat='Latitude', lon='Longitude',
                            size=size, color=color,
                            hover_name='State', zoom=3,
                            mapbox_style='carto-positron',
                            title=f'Shows the {size} & {color} of Indian States.')
    st.plotly_chart(fig, True)
else:
    choice_menu_dict = {'Household Size': household_size,
                        'Religion': religion,
                        'Household Number': household_number,
                        'SC/ST': caste,
                        'Education': education,
                        'Age Groups': age_groups}
    choice = st.sidebar.selectbox('Choose analysis', choice_menu_dict.keys())

    # State selection
    sl_state = st.sidebar.multiselect('Select Indian States', list(state['State']),
                                      ['Bihar', 'Kerala', 'Madhya Pradesh'],
                                      max_selections=5)

    # DataFrame selection based on slected states
    df = choice_menu_dict[str(choice)].query('State==@sl_state')

    # Plots: treemap, sunbrust
    treemap = px.treemap(df, path=[px.Constant('India'), 'State', 'Variable'],
                         values='Value', color='Value', height=1000, width=800)
    sunbrust = px.sunburst(df, path=['State', 'Variable'], values='Value',
                           height=1000, width=500)

    st.plotly_chart(treemap, True, theme=None)
    with st.expander('Sunbrust Plot', False):
        st.plotly_chart(sunbrust, True)
