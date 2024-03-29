""" India 2011 census dashboard with streamlit and python. """

import plotly.express as px
import streamlit as st
from pandas import read_csv

from utils.melt_dataset import melt_dataset

# Page config
st.set_page_config('Districts Analysis', '🌄', 'wide')

# --- Import datasets ---
district = read_csv('data/District_census_2011.csv')
(
    religion,
    household_number,
    caste,
    education,
    household_size,
    age_groups,
) = melt_dataset(district, True)

# --- Sidebar ---
st.sidebar.title('Census 2011')
plot_type = st.sidebar.selectbox('Choose plot type', ['Maps', '2D Plots'])

if plot_type == 'Maps':
    choice_menu = [
        'Population',
        'Sex Ratio',
        'Literacy Rate',
        'Male Literacy Rate',
        'Female Literacy Rate',
    ]
    size = st.sidebar.selectbox('Choose size', choice_menu)
    color = st.sidebar.selectbox('Choose color', choice_menu, 2)
    # --- --- --- --- --- --- --- --- --- --- #
    fig = px.scatter_mapbox(
        district,
        lat='Latitude',
        lon='Longitude',
        size=size,
        color=color,
        hover_name='District',
        zoom=4,
        mapbox_style='carto-positron',
        title=f'Shows the {size} & {color} of Indian Districts.',
        height=900,
    )

    st.plotly_chart(fig, True, theme=None)
else:
    choice_menu_dict = {
        'Household Size': household_size,
        'Religion': religion,
        'Household Number': household_number,
        'SC/ST': caste,
        'Education': education,
        'Age Groups': age_groups,
    }
    choice = st.sidebar.selectbox('Choose analysis', choice_menu_dict.keys())

    # State selection
    sl_state = st.sidebar.multiselect(
        'Select Indian States',
        district['State'].unique(),
        ['Bihar', 'Uttar Pradesh', 'Gujarat'],
        max_selections=5,
    )

    # DataFrame selection based on slected states
    df = choice_menu_dict[str(choice)].query('State==@sl_state')

    # Plots: treemap, sunbrust
    treemap = px.treemap(
        df,
        path=[px.Constant('India'), 'State', 'District', 'Variable'],
        values='Value',
        color='Value',
        height=1000,
        width=800,
    )
    sunbrust = px.sunburst(
        df,
        path=[px.Constant('India'), 'State', 'District', 'Variable'],
        values='Value',
        height=1000,
        width=500,
    )

    with st.expander('Treemap Plot', True):
        st.plotly_chart(treemap, True, theme=None)
    with st.expander('Sunbrust Plot'):
        st.plotly_chart(sunbrust, True, theme=None)
