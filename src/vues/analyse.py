import streamlit as st
from src.router import redirect 
import pandas as pd 
import matplotlib.pyplot as plt 
from pandas import DataFrame, read_csv
import seaborn as sns

def load_view():

    st.markdown("Analyse de données")
    


def load_view():

    st.markdown("**context**:")
    st.markdown("La malnutrition est un problème mondial à la fois extrêmement grave et insuffisamment pris en compte. Elle a un coût humain et économique immense, surtout pour les populations pauvres, ainsi que pour les femmes et les enfants. ")

    df = read_csv("src/assets/malnutrition-estimates.csv")
    st.dataframe(df)

    df1 = read_csv("src/assets/country-wise-average.csv")
    st.dataframe(df1)



    st.markdown("Analyses des donneés")


    st.markdown("""**classement des pays les plus touchées par la malnutritions dans le monde :**""")

    
    
    fig = plt.figure(figsize=(3.5,5))
    ax = fig.add_subplot()
    ax.yaxis.tick_right()
    ax.xaxis.tick_top()
    ax.invert_xaxis()
    top = df.sort_values("Severe Wasting", ascending=False).head(10)
    sns.barplot(data=top, y="Country",   x="Severe Wasting", ax=ax)
    plt.title(label="le top 10 des pays les  plus touchées par la   malnutritions",fontsize=10,fontstyle='oblique')
    st.pyplot(fig)




    st.markdown("""**identifier la classe socile la plus touchées par la malnutritions :**""")



    fig = plt.figure()
    sns.boxplot(data=df1, y="Severe Wasting",   x="Income Classification")
    plt.title(label="la corrélations entre la classe sociale et  l'amaigrissement sévère :  ",fontsize=10,fontstyle='oblique')
    st.pyplot(fig)


    fig = plt.figure(figsize=(10,30))
    sns.scatterplot(data=df, y="Country",  x="Severe Wasting" ,  hue="Income Classification")
    st.pyplot(fig)

    st.markdown("""**l'évolutions du retard de croissance aux fil des années :**""")



    fig = plt.figure(figsize=(35,10))
    sns.lineplot(data=df,  y="Stunting",   x="Year")
    st.pyplot(fig)


    st.markdown("""**l'évolution de la population aux fil des années :**""")

    fig = plt.figure()
    sns.lineplot(data=df, y="U5 Population ('000s)",   x="Stunting")
    plt.title(label="la croissance démographique en fonction des années ",fontsize=10,fontstyle='oblique')

    st.pyplot(fig)


    st.markdown("""**identifier le lien entre le   LLDC et  le LIFD :**""")


    fig = plt.figure()
    sns.violinplot(data=df, y="LIFD", x="LDC")
    plt.title(label="la corrélation  entre LLDC et LIFD ",fontsize=10,fontstyle='oblique')
    st.pyplot(fig)


    if st.button("Analyse de données"): 
        redirect("/login", reload=True)
