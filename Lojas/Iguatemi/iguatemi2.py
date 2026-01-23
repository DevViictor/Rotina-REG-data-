import streamlit as st
import pandas as pd
from data.db import conexao
from PIL import Image
from datetime import datetime
from zoneinfo import ZoneInfo
from data.db import registrar_folga


def tarefas_andressa():
    
    #configuração de pagina

    icon = Image.open("image/vivo.png")
    st.set_page_config(page_title="Registros", page_icon=icon, layout="wide")

    image_logo = Image.open("image/Image (2).png")

    cola, colb, colc = st.columns([4,1,1])

    with colc:
            st.image(image_logo)

    with cola:
            st.title("📝 R.E.G - ABERTURA")

    menu = st.sidebar.radio(
         "Menu",
         ["Tarefas","Registros"])
    
    if menu == "Tarefas":
        
        st.subheader("Painel de tarefas")

        #Dados da tarefa 
        @st.cache_data(ttl=60)
        def carregar_dados():
            conn = conexao()

            sql = """ SELECT * FROM tarefas""" 

            df = pd.read_sql(sql,conn)

            conn.close()
            return df
        
        #Dados dos registros 
    
    
        df= carregar_dados()

        df_abertura = df[df["gl"] == "GLS(ABERTURA)"].copy()

        df_abertura["registrar"] = False
        df_abertura["observacao"] = ""

        editado = st.data_editor(
            
        df_abertura,

        hide_index=True,

        use_container_width=True,

        column_config={
            "registrar": st.column_config.CheckboxColumn("registrar"),
            "observacao": st.column_config.TextColumn(
                "observação",
                help="Digite uma observação se necessário"
            )
            
        },
        disabled=df_abertura.columns.drop(["registrar","observacao"])
    )
        

        def registrar_tarefas(df_selecionado):

            FUSO_BR = ZoneInfo("America/Sao_Paulo")

            agora = datetime.now(FUSO_BR)

            data_atual = agora.date()
            hora_atual = agora.time().replace(microsecond=0)


            conn = conexao()
            cursor = conn.cursor()

            sql = """
                INSERT INTO registros (
                
                titulo,
                descricao,
                periodo,
                gl,
                loja,
                data,
                hora,
                observacao
                )
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                ON CONFLICT ON CONSTRAINT unique_registro DO NOTHING
                """
            
            for _, row in df_selecionado.iterrows():
                
                cursor.execute(sql, (
                    
                    row["titulo"],
                    row["descricao"],
                    row["gl"],
                    "Andressa",
                    "IGUATEMI ||",
                    data_atual,        
                    hora_atual,
                    row["observacao"]               
                ))
                
            
            conn.commit()
            conn.close()


        col1,col2 = st.columns(2)

        with col1:
            if st.button("📌 Registrar tarefas"):

                selecionados = editado[editado["registrar"] == True]

                if selecionados.empty:
                    st.warning("⚠️ Nenhuma tarefa selecionada")
                else:
                    registrar_tarefas(selecionados)
                    st.success("✅ Tarefas registradas com sucesso!")
                st.cache_data.clear()
                st.rerun()


        with col2:
            if st.button("Registrar folga"):
                FUSO_BR = ZoneInfo("America/Sao_Paulo")

                agora = datetime.now(FUSO_BR)

                data_atual = agora.date()
                
                gl = "Andressa"
                loja= "IGUATEMI ||"
                data = data_atual

                registrar_folga(gl,loja,data)
                st.success("Folga registrada ✅")
        
        
    
    if menu == "Registros":

        @st.cache_data(ttl=60)
        def carregar_registros():
            conn = conexao()

            sql = """ SELECT id,titulo,gl,hora,data FROM registros""" 

            dfr = pd.read_sql(sql,conn)
            dfr["data"] = pd.to_datetime(dfr["data"])
            conn.close()
            return dfr
        
        dfr = carregar_registros()

        st.subheader("Tarefas concluídas")

        periodo = st.date_input(
        "Selecione o período",
        value=(
            dfr["data"].max().date(),
            dfr["data"].max().date()
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

        df_periodo = dfr[
        (dfr["gl"] == "Andressa") &
        (dfr["data"] >= data_inicio) &
        (dfr["data"] <= data_fim)
        ].copy()

    
    
        if df_periodo.empty:
            st.info("Não existem registros para o período selecionado.")
        else:
            st.dataframe(df_periodo)
    

def tarefas_diego():
    
    #configuração de pagina

    icon = Image.open("image/vivo.png")
    st.set_page_config(page_title="Registros", page_icon=icon, layout="wide")

    image_logo = Image.open("image/Image (2).png")

    cola, colb, colc = st.columns([4,1,1])

    with colc:
            st.image(image_logo)

    with cola:
            st.title("📝 R.E.G - FECHAMENTO")

    menu = st.sidebar.radio(
         "Menu",
         ["Tarefas","Registros"])
    
    if menu == "Tarefas":
        
        st.subheader("Painel de tarefas")

        #Dados da tarefa 
        @st.cache_data(ttl=60)
        def carregar_dados():
            conn = conexao()

            sql = """ SELECT * FROM tarefas""" 

            df = pd.read_sql(sql,conn)

            conn.close()
            return df
        
        #Dados dos registros 
    
    
        df= carregar_dados()

        df_abertura = df[df["gl"] == "GLS(FECHAMENTO)"].copy()

        df_abertura["registrar"] = False
        df_abertura["observacao"] = ""

        editado = st.data_editor(
            
        df_abertura,

        hide_index=True,

        use_container_width=True,

        column_config={
            "registrar": st.column_config.CheckboxColumn("registrar"),
            "observacao": st.column_config.TextColumn(
                "observação",
                help="Digite uma observação se necessário"
            )
            
        },
        disabled=df_abertura.columns.drop(["registrar","observacao"])
    )
        

        def registrar_tarefas(df_selecionado):

            FUSO_BR = ZoneInfo("America/Sao_Paulo")

            agora = datetime.now(FUSO_BR)

            data_atual = agora.date()
            hora_atual = agora.time().replace(microsecond=0)


            conn = conexao()
            cursor = conn.cursor()

            sql = """
                INSERT INTO registros (
                
                titulo,
                descricao,
                periodo,
                gl,
                loja,
                data,
                hora,
                observacao
                )
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                ON CONFLICT ON CONSTRAINT unique_registro DO NOTHING
                """
            
            for _, row in df_selecionado.iterrows():
                
                cursor.execute(sql, (
                    
                    row["titulo"],
                    row["descricao"],
                    row["gl"],
                    "Diego",
                    "IGUATEMI ||",
                    data_atual,        
                    hora_atual,
                    row["observacao"]               
                ))
                
            
            conn.commit()
            conn.close()


        col1,col2 = st.columns(2)

        with col1:
            if st.button("📌 Registrar tarefas"):

                selecionados = editado[editado["registrar"] == True]

                if selecionados.empty:
                    st.warning("⚠️ Nenhuma tarefa selecionada")
                else:
                    registrar_tarefas(selecionados)
                    st.success("✅ Tarefas registradas com sucesso!")
                st.cache_data.clear()
                st.rerun()


        with col2:
            if st.button("Registrar folga"):
                FUSO_BR = ZoneInfo("America/Sao_Paulo")

                agora = datetime.now(FUSO_BR)

                data_atual = agora.date()
                
                gl = "Diego"
                loja= "IGUATEMI ||"
                data = data_atual

                registrar_folga(gl,loja,data)
                st.success("Folga registrada ✅")
        
        
    
    if menu == "Registros":

        @st.cache_data(ttl=60)
        def carregar_registros():
            conn = conexao()

            sql = """ SELECT id,titulo,gl,hora,data FROM registros""" 

            dfr = pd.read_sql(sql,conn)
            dfr["data"] = pd.to_datetime(dfr["data"])
            conn.close()
            return dfr
        
        dfr = carregar_registros()

        st.subheader("Tarefas concluídas")

        periodo = st.date_input(
        "Selecione o período",
        value=(
            dfr["data"].max().date(),
            dfr["data"].max().date()
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

        df_periodo = dfr[
        (dfr["gl"] == "Diego") &
        (dfr["data"] >= data_inicio) &
        (dfr["data"] <= data_fim)
        ].copy()

    
    
        if df_periodo.empty:
            st.info("Não existem registros para o período selecionado.")
        else:
            st.dataframe(df_periodo)
    