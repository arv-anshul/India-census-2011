""" Overall analysis of census 2011 data. """

import plotly.express as px
import streamlit as st
from pandas import read_csv
from utils.wide_to_long import wide_to_long

# Page config
st.set_page_config('Overall Analysis', '🏞', 'wide')

# --- Import datasets ---
state = read_csv('data/State_census_2011.csv')
(religion, household_number, caste,
 education, household_size, age_groups) = wide_to_long(state, 'State')

# --- Sidebar ---
st.sidebar.title('Cenuse 2011')
choice_menu_dict = {'Household Size': household_size,
                    'Religion': religion,
                    'Household Number': household_number,
                    'SC/ST': caste,
                    'Education': education,
                    'Age Groups': age_groups}
choice = st.sidebar.selectbox('Choose analysis', choice_menu_dict.keys())

# DataFrame selection based on slected states
df = choice_menu_dict[str(choice)]

# Plots: treemap, sunbrust
treemap = px.treemap(df, path=[px.Constant('India'), 'Variable'],
                     values='Value', color='Value', height=700, width=800)
sunbrust = px.sunburst(df, path=[px.Constant('India'), 'Variable'],
                       values='Value', height=700, width=800)

# Scatter plot
with st.expander(':chart_with_upwards_trend: Scatter Plot', True):
    col1, col2, col3 = st.columns(3)
    options = state.columns.drop(state.columns[2:-6])[1:]
    x = col1.selectbox('Select X parameter', options, 4)
    y = col2.selectbox('Select Y parameter', options, 3)
    size = col3.selectbox('Select size parameter', options)

    scatter = px.scatter(state, x, y, 'State', size=size, height=600)
    st.plotly_chart(scatter, True)
with st.expander(':evergreen_tree: Treemap Plot'):
    st.plotly_chart(treemap, True)
with st.expander(':sun_with_face: Sunbrust Plot'):
    st.plotly_chart(sunbrust, True)
