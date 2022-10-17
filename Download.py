import pandas as pd
import streamlit as st
import os
from filter import *
# full_data_url=st.secrets["S_DOWN_URL"]
# size='small'
@st.cache
def load_model(down_url):
    url='https://drive.google.com/uc?id=' + down_url.split('/')[-2]
    try:
        data = pd.read_feather(url)
    except:
        data = pd.read_parquet(url)
    return data
def Download(dict):
    style=""
    expander=dict[0]
    size_style_clicked=dict[1]
    size_style_unclicked = dict[2]
    st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)
    ############################################
    sizes = ['small', 'medium', 'large']
    down_link_names = ['tmdb_50K', 'tmdb_1L', 'tmdb_3_3L']
    d3={}
    col1, col2 = st.columns([5, 1])
    #     st.sidebar.selectbox('Right Side', ['Small', 'Medium', 'Large'])
    with col2:
        original_title = '<p style="font-family:Courier; color:transparent; font-size: 10px;">2</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        with expander.expander('Size'):
            for x in range(3):
                d3[sizes[x]] = st.button(sizes[x],key=sizes[x])
                d3[down_link_names[x]]=st.secrets[down_link_names[x]]
    size=sizes[0]

    down_url=d3[down_link_names[0]]
    x='old'
    for x in range(3):
        if d3[sizes[x]]:
            size = sizes[x]
            down_url=d3[down_link_names[x]]
            # st.markdown(down_url)
            style_para = {'x': x + 1, 'y': 3 - x}
            style += size_style_clicked % style_para
        else:
            style_para = {'x': x + 1, 'y': 3 - x}
            style += size_style_unclicked % style_para
    st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)
    df=load_model(down_url)
    x='updated'

    # st.title('Download Data With Filter')
    import streamlit.components.v1 as components
    from pandas.api.types import (
        is_categorical_dtype,
        is_datetime64_any_dtype,
        is_numeric_dtype,
        is_object_dtype,
    )
    with col1:
        st.markdown(f'Dataset has {df.shape[0]} Rows')
        modify = st.checkbox("Add filters")
    df=df.dropna(subset='vote_count').reset_index(drop=True)
    df['vote_count']=df['vote_count'].apply(lambda x:round(x))
    df=df[['title','original_language','vote_average', 'vote_count',
        'tagline','overview','adult', 'backdrop_path', 'belongs_to_collection',
        'budget', 'genres','homepage', 'id', 'imdb_id',  'original_title',
         'popularity', 'poster_path', 'production_companies',
        'production_countries', 'release_date', 'revenue', 'runtime',
        'spoken_languages', 'status',  'video'
            ]]

    filtered_df =filter_dataframe(df,modify)
    st.dataframe(filtered_df[:5000])
    to_csv = filtered_df.to_csv()
    st.download_button(label='📥 Download Current Result',
                                data=to_csv,
                                file_name= 'filtered_df.csv')
