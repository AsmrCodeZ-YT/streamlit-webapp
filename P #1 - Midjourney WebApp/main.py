# owner2plusai WebApp Midjourney

import streamlit as st
import requests
import io
from PIL import Image


st.set_page_config(
    page_title="Midjourney",
    page_icon="🤖",
)

background = [
    "https://r4.wallpaperflare.com/wallpaper/951/583/798/fantasy-art-warrior-dark-souls-iii-dark-souls-wallpaper-5930c82d514a9d8bd637b87f30d1e6dd.jpg",
    "https://r4.wallpaperflare.com/wallpaper/663/947/813/oldboy-japanese-digital-art-artwork-wallpaper-296078ad614a0d8b962738ff3061568d.jpg",
    "https://r4.wallpaperflare.com/wallpaper/708/846/337/anime-demon-slayer-kimetsu-no-yaiba-tanjirou-kamado-hd-wallpaper-19d0389db1ba2deb26a7684f2051864d.jpg",
    "https://r4.wallpaperflare.com/wallpaper/275/953/312/3d-digital-art-abstract-simple-background-wallpaper-c980b83d513addcbd6c778dfb011b63d.jpg",    
]

# webapp
# VIP::::: loggin in hugginface and take api key

API_KEY = "" #set api key here

try:
    with open(r"styles.css" , "r") as css:
        st.markdown(f"""<style>{css.read()}</style>""" %background[0] , unsafe_allow_html=True)
    
    
    st.get_option("theme.primaryColor")
    st.markdown("""<style>
                #midjourney > div > span{
                    font-family: "Ubuntu Mono", sans-serif;
                    font-weight: 700;
                    color: rgb(250, 250, 199);
                    padding: 0px;
                    margin-left: 40%;
                    line-height: 1.2;
                }
                </style>""",unsafe_allow_html=True)
    st.title("Midjourney")
    promt = st.chat_input("Type Here .... ")
    
    ###########################
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {"Authorization": API_KEY}
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content
    image_bytes = query({
        "inputs": promt,
    })
    ########################### show image 
    image = Image.open(io.BytesIO(image_bytes))
    image.resize((800,600))
    st.image(image.resize((800,600)),promt)
except:
    pass
