import streamlit as st
from datetime import datetime, timedelta
from evecon_api import Evocon
import plotly.graph_objects as go

import base64
from pathlib import Path

st.set_page_config(page_title="PLEC.solutions",
                     page_icon=":bar_chart:",
                     layout="wide")

def img_to_html(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    img_html = "<img src='data:image/png;base64,{}' width=300 >".format(encoded)
    return img_html

st.session_state["body_markdown"] = """
        <style>
               .block-container {
                    padding-top: 2rem;
                    padding-bottom: 5rem;
                    padding-left: 3rem;
                    padding-right: 3rem;
                }
        </style>
        """
st.session_state["header_image_markdown"] = '</div><div style="text-align: right; margin-left: 50%; height: 100px; ">' + '</div></div>'
st.markdown(st.session_state["body_markdown"], unsafe_allow_html=True)
st.markdown(st.session_state["header_image_markdown"], unsafe_allow_html=True)

st.markdown('<div style="text-align: center;"><h1>PLEC Solutions</h1></div>', unsafe_allow_html=True)
### Date picker
today = datetime.now()
pre_five = today - timedelta(days = 10)
lower_limit = datetime(2024, 1, 1)
upper_limit = datetime(2024, 12, 31)

times = st.date_input(
    "Sorgu aralığını seçiniz (Varsayılan son 10 gün):",
    (pre_five, today),
    lower_limit,
    upper_limit,
    format="YYYY.MM.DD",
)

try:
    startTime, endTime = times
except:
    startTime = times
    endTime = datetime.now()

options = ["oee", "losses", "clientmetrics", "checklists"]

username = st.text_input(
    "Username:",
    placeholder="username")
password = st.text_input(
    "Password:",
    placeholder="password",type='password')

if st.button("Sorgula"):
    ev_api = Evocon(username, password, startTime, endTime)
    st.session_state["api"] = ev_api
