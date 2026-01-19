import pandas as pd
import streamlit as st
from db import conexao
from PIL import Image


def visualizar_tarefas():

    icon = Image.open("image/vivo.png")
    st.set_page_config(page_title="Tarefas", page_icon=icon, layout="wide")

    image_logo = Image.open("image/Image (2).png")

    cola, colb, colc = st.columns([4,1,1])

    with colc:
            st.image(image_logo)

    with cola:
            st.title("📝 R.E.G - TAREFAS")

    periodos = ["GLS(ABERTURA)", "GLS(INTERMEDIO)", "GLS(FECHAMENTO)","ITINERANTES"]


    periodo = st.selectbox("Selecione o período",periodos)

    st.subheader("Painel de tarefas")

    def carregar_tarefa(periodo):
           conn = conexao()
           
           sql = "SELECT * FROM tarefas WHERE gl = %s ORDER BY data ASC"
           params = (periodo,)

           df = pd.read_sql(sql, conn, params=params)
           conn.close()
           return df

    df = carregar_tarefa(periodo)

    df["Excluir"] = False

    editado = st.data_editor(
    df,
    hide_index=True,
    use_container_width=True,
    column_config={
        "Excluir": st.column_config.CheckboxColumn("Excluir")
    },
    disabled=df.columns.drop("Excluir")
   )
    
    if df.empty:
        st.info("Nenhum registro adicionado")
    
    editado["Excluir"] = editado["Excluir"].fillna(False)
    
    ids_excluir = editado.loc[editado["Excluir"], "id"].tolist()

    def excluir_tarefas(ids):
                conn = conexao()
                cur = conn.cursor()

                cur.execute(
                "DELETE FROM tarefas WHERE id = ANY(%s)",
                (ids,)
                )

                conn.commit()
                conn.close()

    
    if st.button("🗑️ Excluir selecionados", disabled=not ids_excluir):
        excluir_tarefas(ids_excluir)
        st.cache_data.clear()
        st.rerun()
