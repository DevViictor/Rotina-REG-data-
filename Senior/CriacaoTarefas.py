import streamlit as st
from PIL import Image
from db import inserir_dados,salvar_tarefas
from db import conexao
import pandas as pd


def criar_tarefa():

    icon = Image.open("image/vivo.png")

    st.set_page_config(page_title="R.E.G",
                       layout="wide",
                       page_icon=icon)
    

    # --- HEADER / LOGO ---
    image_logo = Image.open("image/Image (2).png")
    cola, colb, colc = st.columns([4, 1, 1])

    with colc:
        st.image(image_logo)

    with cola:
        st.header("R.E.G - Rotina de Excelência Gerencial")

    def carregar_modelos():
        conn = conexao()
        df = pd.read_sql("SELECT * FROM modelo", conn)
        conn.close()
        return df
    

    df_modelos = carregar_modelos()

    modelo_escolhido = st.selectbox(
    "📋 Modelo de tarefa",
    options=df_modelos["titulo"],
    index=None,
    placeholder="Escolha um modelo"
    )

    if modelo_escolhido:
        modelo = df_modelos[df_modelos["titulo"] == modelo_escolhido].iloc[0]
        titulo = st.session_state.titulo = modelo["titulo"]
        descricao = st.session_state.descricao = modelo["descricao"]


    with st.form("Tarefas"):

        selecãop = ["","GLS(ABERTURA)","GLS(INTERMEDIO)","GLS(FECHAMENTO)","ITINERANTES"]
    
        periodo = st.selectbox("Selecione o periodo : ",selecãop)                           

        titulo = st.text_input("Título da tarefa : ",key="titulo")

        descricao = st.text_input("Descrição da tarfa : ",key="descricao")

        col1,col2 = st.columns(2)
        
        with col1:
            horaI  = st.time_input("Hora inicial : ")

        with col2:
            horaF = st.time_input("Hora Final : ")

        cola,colb = st.columns(2)

        with cola:
            data = st.date_input("Data da tarefa :")

        recorrenciaS= ["","Diária","Semanal","Semanal Laboral(seg a sab)","Mensal","Anual"]
        
        with colb:
            recorrencia = st.selectbox("Tipo de recorrência :",recorrenciaS)

        cold,cole = st.columns(2)

        with cold:
            enviar = st.form_submit_button("Enviar tarefa")
            if enviar:
                inserir_dados(
                    str(periodo),
                    titulo,
                    descricao,
                    horaI,
                    horaF,
                    data,
                    str(recorrencia),
                )
                st.success("Tarefa enviada")
        
        with cole:
            salvar = st.form_submit_button("Salvar modelo")
            if salvar:
    
                salvar_tarefas(
                    titulo,
                    descricao,
                    data
                )
                st.success("Modelo salvo")
                
                

        
            

    
        



    
