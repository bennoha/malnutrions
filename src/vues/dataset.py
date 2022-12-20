import streamlit as st
from src.router import redirect 
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 
from pandas import DataFrame, read_csv
import seaborn as sns

def load_view():

     
    st.markdown("voici nos données brutes ")
    
    df = read_csv("src/assets/malnutrition-estimates.csv")
    st.dataframe(df)

    df1 = read_csv("src/assets/country-wise-average.csv")
    st.dataframe(df1)

    st.markdown("country: c'est la classification des pays les plus touchée par la malnutritions a travers le monde on a principalement les pays de :l'Afrique centrale? l'Amérique latine,et quelques pays de l'assie")

    st.markdown("icone classifications : représente la classe sociale moyenne de la population du pays qui classifiée sur une échelle de 0 a 3:")
    st.markdown("0:  classe  pauvre")
    st.markdown("1classe moyenne ")
    st.markdown("2 haute moyenne ")
    st.markdown("3 haut revenu ")
    
    st.markdown("stunting : c'est le retard de croissance appelée aussi la maldie de Gaucher provoquée soit par une malnutritions ou une sournutritions elle se calcule a partir d'une taille cible ")
    st.markdown("-chez les filles taille cille = taille du père +taille de la mère -13/2 ")
    st.markdown("-chez  les garçons  taille cille = taille du père +taille de la mère +13/2")

    st.markdown("underweight: qui l'insuffisance pondérale ")

    st.markdown("U5 populations: qui correspond a la croissance de la population ")

    st.markdown("le ISO code : c 'est la  Liste des pays dans l’ordre alphabétique et codes de désignation de la norme ISO pour chacun.")

    st.markdown("country : le pays sur lequel l'étude a était faite ")

    st.markdown("Survey Year : c'est l'année de l'enquête ")

    

    if st.button("Jeu de données"): 
        redirect("/login", reload=True)
