import streamlit as st
import psycopg2

# CONEXÃO PARA O BANCO DE DADOS 


def conexao ():
    return psycopg2.connect(
        st.secrets["postgres"]["host"]
       
    )

#tabela de tarefas

conn = conexao()
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS tarefas(
               id SERIAL PRIMARY KEY,
               gl TEXT,
               titulo TEXT,
               descricao TEXT,
               hora_inicial TIME,
               hora_final TIME, 
               data DATE,
               recorrencia TEXT
               );
               """)
conn.commit()
cursor.close()
conn.close()

#tarefaas de registros

conn = conexao()
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS registros(
               id SERIAL PRIMARY KEY,
               titulo TEXT,
               descricao TEXT,
               periodo TEXT,
               gl TEXT,
               loja TEXT,
               data DATE,
               hora TIME,
               observacao TEXT
               ); """)
conn.commit()
cursor.close()
conn.close()

#tabela de folga 

conn =  conexao()
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS folgas(
        id SERIAL PRIMARY KEY,
        gl TEXT,
        loja TEXT,
        data DATE);
               
    """)

conn.commit()
cursor.close()
conn.close()


#tabela de ferias 

conn = conexao()
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS ferias(
               id SERIAL PRIMARY KEY,
               gl TEXT,
               loja TEXT,
               data_saida DATE,
               data_retorno DATE);
""")

conn.commit()
cursor.close()
conn.close()


#DADOS INSERIDOS NA TABELA 
def inserir_dados(periodo,titulo,descricao,horaI,horaF,data,recorrencia):

    conn = conexao()
    cursor = conn.cursor()

    sql = """
    
    INSERT INTO tarefas(
    
    gl,
    titulo,
    descricao,
    hora_inicial,
    hora_final,
    data,
    recorrencia
    )
    VALUES(%s,%s,%s,%s,%s,%s,%s)

    """

    cursor.execute(
    sql,
    (periodo, titulo, descricao, horaI, horaF, data, recorrencia)
    )

    conn.commit()
    cursor.close()
    conn.close()


#Salvar tarefa

def salvar_tarefas(titulo,descricao,data):
 
    conn = conexao()
    cursor = conn.cursor()

    sql = """
        INSERT INTO modelo(
        titulo,
        descricao,
        data
        )
        VALUES(%s,%s,%s)
    """
    cursor.execute(sql,
                   (titulo,descricao,data)
                   )

    conn.commit()
    cursor.close()
    conn.close()

#registrar folga

def registrar_folga(gl,loja,data):

    conn = conexao()
    cursor = conn.cursor()

    sql = """
        INSERT INTO folgas (
        gl,
        loja,
        data
        ) VALUES(%s,%s,%s)
        ON CONFLICT ON CONSTRAINT unique_folga DO NOTHING
    """
    cursor.execute(
    sql,
    (gl,loja,data)
    )

    conn.commit()
    cursor.close()
    conn.close()

#registar ferias

def registar_ferias(gl,loja,data_saida,data_retorno):
    
    conn = conexao()
    cursor = conn.cursor()

    sql = """
        INSERT INTO ferias (
        gl,
        loja,
        data_saida,
        data_retorno
        ) VALUES(%s,%s,%s,%s)
        ON CONFLICT ON CONSTRAINT unique_ferias DO NOTHING
        """
    cursor.execute(
        sql,
        (gl,loja,data_saida,data_retorno)
        )

    conn.commit()
    cursor.close()
    conn.close()