import streamlit as st
from page_1 import page_1_section
from page_2 import page_2_section
from page_3 import page_3_section
from page_4 import page_4_section

st.set_page_config(
    page_title="Dashboard",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)


font_css = """
<style>
   button[data-baseweb="tab"] {
   font-size: 24px;
   margin: 0;
   width: 100%;
   }
</style>
"""

st.write(font_css, unsafe_allow_html=True)


tabs = st.tabs(
    [
        "Penjualan dan Pendapatan",
        "Jumlah Tamu dan Demografi",
        "Profit dan Loss",
    ]
)

with tabs[0]:
    page_1_section()
with tabs[1]:
    page_2_section()
with tabs[2]:
    page_3_section()
