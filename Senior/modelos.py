import pandas as pd
import streamlit as st
from data.db import conexao
from PIL import Image


def modelos_prontos():
    
    icon = Image.open("image/vivo.png")
    st.set_page_config(page_title="Tarefas", page_icon=icon, layout="wide")

    image_logo = Image.open("image/Image (2).png")

    cola, colb, colc = st.columns([4,1,1])

    with colc:
            st.image(image_logo)

    with cola:
            st.title("📝 R.E.G - MODELOS")

    st.cache_data(ttl=60)
    def carregar_modelo():

        conn = conexao()
        
        df_abertura = pd.read_sql("SELECT * FROM modelo",conn)
        conn.close()
        return df_abertura
    
    df = carregar_modelo()

    df["Excluir"] = False

    st.subheader("Painel de modelos salvos")

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
        st.info("Nenhum modelo adicionado")
    
    editado["Excluir"] = editado["Excluir"].fillna(False)
    
    ids_excluir = editado.loc[editado["Excluir"], "id"].tolist()

    def excluir_tarefas(ids):
                conn = conexao()
                cur = conn.cursor()

                cur.execute(
                "DELETE FROM modelo WHERE id = ANY(%s)",
                (ids,)
                )

                conn.commit()
                conn.close()

    
    if st.button("🗑️ Excluir selecionados", disabled=not ids_excluir):
        excluir_tarefas(ids_excluir)
        st.cache_data.clear()
        st.rerun()