import streamlit as st
import os
#################
st.set_page_config(page_title='👻👻🚗🌫️‍', page_icon='👻',
                   layout="wide", initial_sidebar_state="collapsed",
                   menu_items=None)
from Recommender import *
from Download import *
##################
page = st.sidebar.selectbox('Select page',['Recommender','Download Data'])
# st.markdown(os.listdir(os.getcwd()))
header=st.empty()
@st.cache
def load_model(recom_url):
    url='https://drive.google.com/uc?id=' + recom_url.split('/')[-2]
    data = pd.read_feather(url)
    return data
#################
col1, col2 = st.columns([5, 1])
d3 = {}
links1={}
links2={}
recom_link_names=['S_RECOM_URL','M_RECOM_URL','L_RECOM_URL']

sim_link_names=['S_SIM_URL','M_SIM_URL','L_SIM_URL']
sizes = ['small', 'medium', 'large']
with col2:
    original_title = '<p style="font-family:Courier; color:transparent; font-size: 10px;">1</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    expander=st.empty()
    with expander.expander('Size'):
        for x in range(3):
            d3[sizes[x]] = st.button(sizes[x])
            links1[recom_link_names[x]]=st.secrets[recom_link_names[x]]
            # st.markdown(f'{os.getcwd()}{st.secrets}')
            links2[sim_link_names[x]]=st.secrets[sim_link_names[x]]
size=sizes[0]
recom_url=links1[recom_link_names[0]]
sim_url=links2[sim_link_names[0]]
df=load_model(recom_url)
sim=load_model(sim_url)
for x in range(3):
    if d3[sizes[x]]:
        size = sizes[x]
        recom_url=links1[recom_link_names[x]]
        sim_url = links2[sim_link_names[x]]
        df=load_model(recom_url)
        sim=load_model(sim_url)
# st.markdown(f'Sim is {sim.shape}, df is {df.shape}')
# st.markdown(f'main{current_time}-{os.listdir(os.getcwd())}')
movies_list=df['title'].values
movies_list=np.append(movies_list,"")
movies_list=sorted(movies_list)
######################
p=1
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
##################
size = 'medium'
###########################

if page=='Recommender':
    header.title("Movie Recommendations")
    with col1:
        selected_movie = st.selectbox("",
                                      movies_list
                                      )
    Recommender(selected_movie,df,sim)
elif page=='Download Data':
    header.title('Download Data With Filter')
    Download(expander)
    # st.markdown("Download")
