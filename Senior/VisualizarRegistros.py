import pandas as pd
import streamlit as st
from PIL import Image
from db import conexao


def visualizar_registros():

    icon = Image.open("image/vivo.png")
    st.set_page_config(page_title="Registros", page_icon=icon, layout="wide")

    image_logo = Image.open("image/Image (2).png")

    cola, colb, colc = st.columns([4,1,1])

    with colc:
            st.image(image_logo)

    with cola:
            st.title("📝 R.E.G - TAREFAS CONCLUÍDAS")

    #lista de dicionarios , separados por carteira e seus recpetivos gls
    carteiras = {
         
    "TODOS": [
          
            ""],

         
    "CARTEIRA FABIANA": [
          
            "Mércia",
            "Francisca",
            "Vinicius",
            "Vitor",
            "Mailan",
            "Danilo",
            "Vanessa",
            "Crislaine",
            "Neide",
            "Maise",
            "Denise_Parque",
            "Adrielle"],

    "CARTEIRA FELIPE": [
          
            "Max",
            "Denise",
            "Andressa",
            "Diego",
            "Jairo",
            "Wanderlei"],

    "CARTEIRA JHON": [
          
            "Igor",
            "Carol",
            "Alana",
            "Diego",
            "Marcus",
            "Sara",
            "Rafael"],

    "CARTEIRA CHRYS": [
            
            "Camyla",
            "Bruno",
            "Gilvania"],

    "ITINERANTES": [
          
            "Lee",
            "Lázaro",
            "Marcus"
    ]
    
 }
    #conexão com o banco
    @st.cache_data(ttl=60)
    def carregar_tarefas():
        
        conn = conexao()
        
        sql= ("SELECT titulo,gl,data FROM registros")

        df = pd.read_sql(sql,conn)
        
        df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")
        
        conn.close()
        return df

    df = carregar_tarefas()
    

    col1,col2 = st.columns(2)

    # filtro com selectbox
    with col1:
        carteira = st.selectbox(
                "Selecione a carteira",
                options=list(carteiras.keys())
                        )
        
    #filtro de data
    with col2:
        periodo = st.date_input(
        "Selecione o período",
        value=(
                df["data"].min().date(),
                df["data"].max().date()
        )
        ) 
    
    #aviso para seleioncar os periodos
    if not isinstance(periodo, tuple) or len(periodo) != 2:
        st.warning("⚠️ Selecione um período com data inicial e final.")
        st.stop()
    
    #filtrod de data
    data_inicio, data_fim = periodo
        
    data_inicio = pd.to_datetime(data_inicio)
    data_fim = pd.to_datetime(data_fim)

    df_periodo = df[
    (df["data"] >= data_inicio) &
    (df["data"] <= data_fim)
    ]
    
    #seleção para visualização
    if carteira == "TODOS":
        gls_carteira = sorted(df["gl"].unique())
    else:
        gls_carteira = carteiras[carteira]
                
    df_plot = (
    df_periodo.groupby("gl")
    .size()
    .reset_index(name="total")
     )

    df_plot = (
        df_plot
        .set_index("gl")
        .reindex(gls_carteira, fill_value=0)
        .reset_index()
        )
    
    st.bar_chart(df_plot, x="gl", y="total")
    