
import streamlit as st
import pandas as pd
from data.db import registar_ferias
from PIL import Image


def ferias_davila():

    icon = Image.open("image/vivo.png")
    st.set_page_config(page_title="Férias", page_icon=icon, layout="wide")

    image_logo = Image.open("image/Image (2).png")

    cola, colb, colc = st.columns([4,1,1])

    with colc:
            st.image(image_logo)

    with cola:
        st.header("🏖️ R.E.G - FÉRIAS")

    st.subheader("Registro das férias")

    with st.form("Férias"):

        gl = ["","Maise"]
        loja = ["DIAS D´VILA"]

        col1,col2 = st.columns(2)

        with col1:
            
            gls = st.selectbox("Selecione o nome do gl :",gl)

        with col2:
            
            loja = st.selectbox("Loja",loja)

        col3,col4 = st.columns(2)

        with col3:
            
            data_saida = st.date_input("Selecione o dia de início das férias")

        with col4:
            
            data_retorno = st.date_input("Selecione o dia de retorno das férias")

        
        registrar = st.form_submit_button("Registrar Férias")

        if registrar:
             registar_ferias(
                  str(gls),
                  str(loja),
                  data_saida,
                  data_retorno
             )
             st.success("Registrado, bom descanso")



