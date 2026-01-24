import pandas as pd
import streamlit as st
from PIL import Image
from data.db import conexao


def visualizar_registros():

    icon = Image.open("image/vivo.png")
    st.set_page_config(page_title="Registros", page_icon=icon, layout="wide")

    image_logo = Image.open("image/Image (2).png")

    cola, colb, colc = st.columns([4,1,1])

    with colc:
            st.image(image_logo)

    with cola:
            st.title("R.E.G - RELATÓRIOS")

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
    
    opcao = st.sidebar.radio("MENU",["D-1","Folgas","Férias"])

    if opcao == "D-1":
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
                        ,key="folga"       )
                
        #filtro de data
        with col2:
                periodo = st.date_input(
                "Selecione o período",
                value=(
                        df["data"].max().date(),
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


    if opcao == "Folgas":

        @st.cache_data(ttl=60)
        def carregar_folgas():
                
                conn = conexao()
                
                sql= ("SELECT gl,loja,data FROM folgas")

                df = pd.read_sql(sql,conn)
                
                df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")
                
                conn.close()
                return df

        df_folgas = carregar_folgas()

        col1,col2 = st.columns(2)

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
                        df_folgas["data"].max().date(),
                        df_folgas["data"].max().date()
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

        df_periodo = df_folgas[
        (df_folgas["data"] >= data_inicio) &
        (df_folgas["data"] <= data_fim)
        ]

        if carteira == "TODOS":
                gls_carteira = sorted(df_folgas["gl"].unique())
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

    if opcao == "Férias":

        @st.cache_data(ttl=60)
        def carregar_ferias():
                
                conn = conexao()
                
                sql= "SELECT gl, loja, data_saida, data_retorno FROM ferias"

                df = pd.read_sql(sql,conn)
                
                df["data_saida"] = pd.to_datetime(df["data_saida"], format="%d/%m/%Y")
                
                df["data_retorno"] = pd.to_datetime(df["data_retorno"], format="%d/%m/%Y")

                conn.close()
                return df

        df_ferias = carregar_ferias()

        col1,col2 = st.columns(2)

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
                        df_ferias["data_saida"].max().date(),
                        df_ferias["data_saida"].max().date()
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

        df_periodo = df_ferias[
        (df_ferias["data_saida"] >= data_inicio) &
        (df_ferias["data_saida"] <= data_fim)
        ]

        if carteira != "TODOS":
                df_filtrado = df_periodo[
                        df_periodo["gl"].isin(carteiras[carteira])
                ]
        else:
                df_filtrado = df_periodo.copy()

        df_tabela = df_filtrado[[
        "gl",
        "loja",
        "data_saida",
        "data_retorno"

        ]].sort_values("data_saida")

        df_tabela["data_saida"] = df_tabela["data_saida"].dt.strftime("%d/%m/%Y")

        df_tabela["data_retorno"] = df_tabela["data_retorno"].dt.strftime("%d/%m/%Y")
        

        st.subheader("📋 Saídas de férias")
        st.dataframe(
        df_tabela,
        use_container_width=True,
        hide_index=True
        )