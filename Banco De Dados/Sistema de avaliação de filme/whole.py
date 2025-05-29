# streamlit, mariadb e plotly

import mariadb as mdb
import plotly.express as px 
import streamlit as st
import pandas as pd 

CONFIG_BANCO = {
    "host": "10.104.77.36",
    "user": "root",
    "password": "Senai@107",
    "database": "isabelle"
}

def conectar_db():
    conexao = mdb.connector.connect(**CONFIG_BANCO) # conectando com o banco de dados
    cursor = conexao.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS alunos(
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       nome VARCHAR(100) NOT NULL,
                       nota1 FLOAT NOT NULL,
                       nota2 FLOAT NOT NULL,
                       nota3 FLOAT NOT NULL,
                       media FLOAT NOT NULL,
                       situacao VARCHAR(25) NOT NULL )''')
    conexao.commit()
    return conexao, cursor