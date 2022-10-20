import streamlit as st
import os
#################
st.set_page_config(page_title='👻👻🚗🌫️‍', page_icon='👻',
                   layout="centered", initial_sidebar_state="collapsed",
                   menu_items=None)
from Recommender import *
from Download import *
##################
header=st.empty()
header.title('Movie Recommendations')
page = st.sidebar.selectbox('Select page',['Recommender','Download Data'])
# st.markdown(os.listdir(os.getcwd()))
@st.cache
def load_model(recom_url):
    url='https://drive.google.com/uc?id=' + recom_url.split('/')[-2]
    data = pd.read_feather(url)
    return data
######################################
style2=''' h1[id="movie-recommendations"] {
    position: relative;
    top: 100px;} 
    div[data-testid="column"]{
    position: relative;
    top: -180px;
    }
    div[class="element-container css-1hynsf2 e1tzin5v3"]{
    position: relative;
    top: -180px;
    }
    h1[id="trending-now"]{
    position: relative;
    left: 250px;
    top:-30px;
    }
    '''
st.markdown(f"<style>{style2}</style>", unsafe_allow_html=True)
style3=''''''
st.markdown(f"<style>{style3}</style>", unsafe_allow_html=True)
######################################
s1 ="""<style>.st-bf {
    border-color:transparent;
    }
    </style>"""
st.markdown(s1, unsafe_allow_html=True)
#0099ff
#00ff00
# ff0000
#################################
s2 ="""<style>div[data-testid="stVerticalBlock"] > div:nth-child(n+7) button{
    background-color: #ce1126;
    color: white;
    height: 2em;
    width: 8em;
    border-radius:10px;
    border:3px solid #000000;
    font-size:22px;
    font-weight: bold;
    margin: left;
    display: block;
}

div.stButton > button:hover {
	background:linear-gradient(to bottom, red 0%, #ff5a5a 100%);
	background-color:#ce1126;
}

div.stButton > button:active {
	position:relative;
	top:3px;
}

</style>"""
st.markdown(s2, unsafe_allow_html=True)

#################################
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
size_style_unclicked = '''div[data-testid*="stVerticalBlock"] > div:nth-child(%(x)s):nth-last-child(%(y)s) button {
    border - color: red;
    color: white;
    opacity: 1;
    height: 2.2em;
    width: 4.5em;
    border-radius:10px;
    border:3px solid #000000;
    font-size:18px;
    font-weight: normal;
    margin: left;
    display: block;
    box-shadow: rgba(255, 75, 75, 0.5) 0px 0px 0px 0.2rem;
    outline: currentcolor none medium; }'''
size_style_clicked = '''div[data-testid*="stVerticalBlock"] > div:nth-child(%(x)s):nth-last-child(%(y)s) button {
    border - color: yellow;
    color: white;
    opacity: 1;
    height: 2.2em;
    width: 4.5em;
    border-radius:10px;
    border:3px solid #000000;
    font-size:18px;
    font-weight: normal;
    margin: auto;
    display: block;
    background-color: crimson;
    box-shadow: rgba(255, 75, 75, 0.5) 0px 0px 0px 0.2rem;
    outline: currentcolor none medium; }'''
style=""
for x in range(3):
    if d3[sizes[x]]:
        size = sizes[x]
        recom_url=links1[recom_link_names[x]]
        sim_url = links2[sim_link_names[x]]
        df=load_model(recom_url)
        sim=load_model(sim_url)
        style_para={'x':x+1,'y':3-x}
        style += size_style_clicked % style_para
    else:
        style_para = {'x': x + 1, 'y': 3 - x}
        style += size_style_unclicked % style_para
st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)
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
    data_to_downloader=[expander,
                        size_style_clicked,
                        size_style_unclicked]
    # Download(data_to_downloader)
    # st.markdown("Download")
