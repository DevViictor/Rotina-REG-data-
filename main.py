import streamlit as st
from PIL import Image
from Senior.CriacaoTarefas import criar_tarefa
from Senior.VisualizarTarefas import visualizar_tarefas
from Senior.modelos import modelos_prontos
from Senior.VisualizarRegistros import visualizar_registros
from Lojas.Iguatemi.iguatemi import tarefas_max,tarefas_denise
from Lojas.Iguatemi.iguatemi2 import tarefas_diego,tarefas_andressa
from Lojas.Nort.Nort import tarefas_jairo, tarefas_wanderlei
from Lojas.Salvador.Salvador1 import tarefas_francisca,tarefas_mercia,tarefas_vinicius
from Lojas.Salvador.Salvador2 import tarefas_mailan,tarefas_vitor
from Lojas.Bela.Bela import tarefas_danilo,tarefas_vanessa
from Lojas.Paralela.paralela import tarefas_crislaine,tarefas_neide
from Lojas.Parque.parque import tarefas_adrielle,tarefas_deniseP
from Lojas.Davilla.davilla import tarefas_maise
from Lojas.Lapa.lapa import tarefas_rafael,tarefas_sara
from Lojas.Piedade.piedade import tarefas_diegoP,tarefas_marcusp
from Lojas.Barra.Barra import tarefas_alana,tarefas_carol,tarefas_igor
from Lojas.Boulevard.boulevard  import tarefas_bruno,tarefas_camyla,tarefas_gilvania
from Lojas.Itinerante.itinerantes import tarefas_lazaro,tarefas_lee,tarefas_marcus
from Lojas.Ferias.iguatemi_ferias import ferias_iguatemi1,ferias_iguatemi2
from Lojas.Ferias.barra_ferias import ferias_barra
from Lojas.Ferias.bela_ferias import ferias_bela
from Lojas.Ferias.boulevard_ferias  import ferias_boulevard
from Lojas.Ferias.lapa_ferias import ferias_lapa
from Lojas.Ferias.norte_ferias import ferias_norte
from Lojas.Ferias.paralela_ferias import ferias_paralela
from Lojas.Ferias.piedade_ferias import ferias_piedade
from Lojas.Ferias.ssa_ferias import ferias_ssa1,ferias_ssa2
from Lojas.Ferias.parque_ferias import ferias_parque
from Lojas.Ferias.davila_ferias import ferias_davila
from Lojas.Ferias.itinerante_ferias import ferias_itinerantes


st.sidebar.image("image/Image (2).png")

icon = Image.open("image/vivo.png")

st.set_page_config(page_title="Login", page_icon=icon)

usuarios = st.secrets["usuarios"]

# -----------------------------------------
# SESSION STATE
# -----------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.role = None

# -----------------------------------------
# LOGIN
# -----------------------------------------
def login():
   
    st.title("Login")
    user = st.text_input("Usuário:")
    password = st.text_input("Senha:", type="password")

    if st.button("Entrar"):
        if user in usuarios and password == usuarios[user]["senha"]:
            st.session_state.logged_in = True
            st.session_state.user = user
            st.session_state.role = usuarios[user]["role"]
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos!")

# -----------------------------------------
# LOGOUT
# -----------------------------------------
def logout():
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.role = None
    st.rerun()

# -----------------------------------------
# NAVEGAÇÃO
# -----------------------------------------
def run_navigation():
    role = st.session_state.role

    # Criar objetos Page
    
    #Senior

    #criaar tarefas
    Criar_tatarefa = st.Page(criar_tarefa, title="Criar", icon="📋")
    
    #visualização das tarefas
    Visualizar_tarefas = st.Page(visualizar_tarefas, title="Visualizar", icon="📋")

    #visualizaçãod dos modelos 
    Modelos_prontos = st.Page(modelos_prontos, title="Modelos prontos", icon="📋")

    #visualização dos registros
    Visualizar_registros = st.Page(visualizar_registros, title="Relatório", icon="📊")
    
    #Carteira de Felipe

    Tarefas_max =  st.Page(tarefas_max, title="ABERTURA")
    Tarefas_denise =  st.Page(tarefas_denise, title="FECHAMENTO")
    
    Tarefas_andressa =  st.Page(tarefas_andressa, title="ABERTURA")
    Tarefas_diego =  st.Page(tarefas_diego, title="FECHAMENTO")

    Tarefas_jairo = st.Page(tarefas_jairo, title="ABERTURA")
    Tarefas_wanderlei = st.Page(tarefas_wanderlei, title="FECHAMENTO")

    #Carteira Fabiana 

    Tarefas_mercia = st.Page(tarefas_mercia, title="ABERTURA")
    Tarefas_francisca = st.Page(tarefas_francisca, title="INTERMÉDIO")
    Tarefas_vinicius = st.Page(tarefas_vinicius, title="FECHAMENTO")
    
    Tarefas_vitor =st.Page(tarefas_vitor, title="ABERTURA")
    Tarefas_mailan = st.Page(tarefas_mailan, title="FECHAMENTO")

    Tarefas_dainilo = st.Page(tarefas_danilo, title="ABERTURA")
    Tarefas_vanessa = st.Page(tarefas_vanessa, title="FECHAMENTO")

    Tarefas_crislaine = st.Page(tarefas_crislaine, title="ABERTURA")
    Tarefas_neide = st.Page(tarefas_neide, title="FECHAMENTO")

    Tarefas_denisep = st.Page(tarefas_deniseP, title="ABERTURA")
    Tarefas_adrielle = st.Page(tarefas_adrielle, title="FECHAMENTO")

    Tarefas_maise = st.Page(tarefas_maise, title="ABERTURA")

    #Carteira johon

    Tarefas_rafael = st.Page(tarefas_rafael, title="ABERTURA")
    Tarefas_sara =  st.Page(tarefas_sara, title="FECHAMENTO")

    Tarefas_diegop = st.Page(tarefas_diegoP, title="ABERTURA")
    Tarefas_marcusp = st.Page(tarefas_marcusp, title="FECHAMENTO")

    Tarefas_carol = st.Page(tarefas_carol, title="ABERTURA")
    Tarefas_alana = st.Page(tarefas_alana, title="INTERMÉDIO")
    Tarefas_igor = st.Page(tarefas_igor, title="FECHAMENTO")

    #Carteira chrys

    Tarefas_bruno = st.Page(tarefas_bruno, title="ABERTURA")
    Tarefas_camyla = st.Page(tarefas_camyla, title="INTERMÉDIO")
    Tarefas_gilvania = st.Page(tarefas_gilvania, title="FECHAMENTO")

    #Itinerantes
    Tarefas_lee = st.Page(tarefas_lee, title="Suas tarefas")
    Tarefas_marcus = st.Page(tarefas_marcus, title="Suas tarefas")
    Tarefas_lazaro = st.Page(tarefas_lazaro, title="Suas tarefas")

    #Ferias

    #Carteira felipe

    Ferias_iguatemi1 = st.Page(ferias_iguatemi1, title="R.E.G - FÉRIAS")
    Ferias_iguatemi2 = st.Page(ferias_iguatemi2, title="R.E.G - FÉRIAS")
    Ferias_norte = st.Page(ferias_norte, title="R.E.G - FÉRIAS")

    #Carteira Fabiana

    Ferias_ssa1 = st.Page(ferias_ssa1, title="R.E.G - FÉRIAS")
    Ferias_ssa2 = st.Page(ferias_ssa2, title="R.E.G - FÉRIAS")
    Ferias_bela = st.Page(ferias_bela, title="R.E.G - FÉRIAS")
    Ferias_paralela = st.Page(ferias_paralela, title="R.E.G - FÉRIAS")
    Ferias_parque = st.Page(ferias_parque, title="R.E.G - FÉRIAS")
    Ferias_davila = st.Page(ferias_davila, title="R.E.G - FÉRIAS")
    
    #Carteira John
    Ferias_piedade = st.Page(ferias_piedade, title="R.E.G - FÉRIAS")
    Ferias_lapa = st.Page(ferias_lapa, title="R.E.G - FÉRIAS") 
    Ferias_barra = st.Page(ferias_barra, title="R.E.G - FÉRIAS") 
    
    #Carteira Chrys
    Ferias_boulevard = st.Page(ferias_boulevard, title="R.E.G - FÉRIAS")

    #Itinerantes
    Ferias_itinerantes = st.Page(ferias_itinerantes, title="R.E.G - FÉRIAS")

    # Menus por role
    if role == "Victor":

        menu = {
            "R.E.G": [
                Visualizar_registros
                
            ]
        }

        menu2 = {
            "Opções de tarefa": [
                Criar_tatarefa,
                Visualizar_tarefas,
                Modelos_prontos
            ]
        }

        menu3 = {
            "NADA": [
               
            ]
        }

        menu4 = {
            "Nada": [
                
            ]
        }

    if role == "Iguatemi1":

        menu = {
            "GLS(ABERTURA)": [
                Tarefas_max
                
            ]
        }

        menu2 = {
            "GLS(FECHAMENTO)": [
                Tarefas_denise


            ]
        }

        menu3 = {
            "REGISTRAR FÉRIAS": [
               Ferias_iguatemi1
            ]
        }

        menu4 = {
            "Nada": [
                
            ]
        }
    

    if role == "Iguatemi2":

        menu = {
            "GLS(ABERTURA)": [
                Tarefas_andressa
                
            ]
        }

        menu2 = {
            "GLS(FECHAMENTO)": [
                Tarefas_diego


            ]
        }

        menu3 = {
            "REGISTRAR FÉRIAS": [
                Ferias_iguatemi2
               
            ]
        }

        menu4 = {
            "Nada": [
                
            ]
        }

    if role == "Norte":

        menu = {
            "GLS(ABERTURA)": [
                Tarefas_jairo
                
            ]
        }

        menu2 = {
            "GLS(FECHAMENTO)": [
                Tarefas_wanderlei

            ]
        }

        menu3 = {
            "REGISTRAR FÉRIAS": [
               Ferias_norte
            ]
        }

        menu4 = {
            "Nada": [
                
            ]
        }
    
    if role == "Salvador1":

        menu = {
            "GLS(ABERTURA)": [
                Tarefas_mercia
                
            ]
        }

        menu2 = {
            "GLS(INTERMÉDIO)": [
                Tarefas_francisca
            ]
        }

        menu3 = {
            "GLS(FECHAMENTO)": [
                Tarefas_vinicius
            ]
        }

        menu4 = {
            "REGISTRAR FÉRIAS": [
                Ferias_ssa1
            ]
        }
    
    if role == "Salvador2":

        menu = {
            "GLS(ABERTURA)": [
                Tarefas_vitor
                
            ]
        }

        menu2 = {
            "GLS(FECHAMENTO)": [
                Tarefas_mailan
            ]
        }

        menu3 = {
            "REGISTRAR FÉRIAS": [
                Ferias_ssa2
            ]
        }

        menu4 = {
            "Nada": [
                
            ]
        }

    if role == "Bela":

        menu = {
            "GLS(ABERTURA)": [
                Tarefas_dainilo
                
            ]
        }

        menu2 = {
            "GLS(FECHAMENTO)": [
                Tarefas_vanessa
            ]
        }

        menu3 = {
            "REGISTRAR FÉRIAS": [
                Ferias_bela
            ]
        }

        menu4 = {
            "Nada": [
                
            ]
        }
    
    if role == "Paralela":

        menu = {
            "GLS(ABERTURA)": [
                Tarefas_crislaine
                
            ]
        }

        menu2 = {
            "GLS(FECHAMENTO)": [
                Tarefas_neide
            ]
        }

        menu3 = {
            "REGISTRAR FÉRIAS": [
                Ferias_paralela
            ]
        }

        menu4 = {
            "Nada": [
                
            ]
        }
    
    if role == "Parque":

        menu = {
            "GLS(ABERTURA)": [
                Tarefas_denisep
                
            ]
        }

        menu2 = {
            "GLS(FECHAMENTO)": [
                Tarefas_adrielle
            ]
        }

        menu3 = {
            "REGISTRAR FÉRIAS": [
                Ferias_parque
            ]
        }

        menu4 = {
            "Nada": [
                
            ]
        }
    
    if role == "Davila":

        menu = {
            "GLS(ABERTURA)": [
                Tarefas_maise
                
            ]
        }

        menu2 = {
            "REGISTRAR FÉRIAS": [
                Ferias_davila
            ]
        }

        menu3 = {
            "nada": [
                
            ]
        }

        menu4 = {
            "Nada": [
                
            ]
        }
    
    if role == "Lapa":

        menu = {
            "GLS(ABERTURA)": [
                Tarefas_rafael
                
            ]
        }

        menu2 = {
            "GLS(FECHAMENTO)": [
                Tarefas_sara
                
            ]
        }

        menu3 = {
            "REGISTRAR FÉRIAS": [
                Ferias_lapa
            ]
        }

        menu4 = {
            "Nada": [
                
            ]
        }

    if role == "Piedade":

        menu = {
            "GLS(ABERTURA)": [
                Tarefas_diegop
                
            ]
        }

        menu2 = {
            "GLS(FECHAMENTO)": [
                Tarefas_marcusp
                
            ]
        }

        menu3 = {
            "REGISTRAR FÉRIAS": [
                Ferias_piedade
                
            ]
        }

        menu4 = {
            "Nada": [
                
            ]
        }
    
    if role == "Barra":

        menu = {
            "GLS(ABERTURA)": [
                Tarefas_carol
                
            ]
        }

        menu2 = {
            "GLS(INTERMÉDIO)": [
                Tarefas_alana



            ]
        }

        menu3 = {
            "GLS(FECHAMENTO)": [
                Tarefas_igor
            ]
        }

        menu4 = {
            "REGISTRAR FÉRIAS": [
                Ferias_barra
            ]
        }
    
    if role == "Boulevard":

        menu = {
            "GLS(ABERTURA)": [
                Tarefas_bruno
                
            ]
        }

        menu2 = {
            "GLS(INTERMÉDIO)": [
                Tarefas_camyla

            ]
        }

        menu3 = {
            "GLS(FECHAMENTO)": [
                Tarefas_gilvania
            ]
        }

        menu4 = {
            "REGISTRAR FÉRIAS": [
                Ferias_boulevard
            ]
        }
    
    if role == "Itinerantes":

        menu = {
            "Lee": [
                Tarefas_lee
                
            ]
        }

        menu2 = {
            "Marcus": [
                Tarefas_marcus

            ]
        }

        menu3 = {
            "Lázaro": [
                Tarefas_lazaro
            ]
        }

        menu4 = {
            "REGISTRAR FÉRIAS": [
                Ferias_itinerantes
            ]
        }
    


    # Criar navegação
    
    soma = {**menu,**menu2,**menu3,**menu4}

    nav = st.navigation(soma)


    # Sidebar com usuário
    st.sidebar.write(f"👤 Usuário: **{st.session_state.user}**")
    st.sidebar.button("Sair", on_click=logout)

    # Rodar página selecionada
    nav.run()

# -----------------------------------------
# EXECUÇÃO PRINCIPAL
# -----------------------------------------
if not st.session_state.logged_in:
    login()
else:
    run_navigation()
