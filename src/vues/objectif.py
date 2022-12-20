import streamlit as st
from src.router import redirect 

def load_view():

    st.markdown("objectif du projet")
    
    st.markdown("**Repondre a la problématique**:")
    st.markdown("l'identifications  des  pays les plus touchés par la malnutritions  a travers le monde  et l'impacte de la crise économique  mondial de 2008 sur l'évolutions de la malnutritions   dans  ses pays la .")
    if st.button("ojectif du projet"): 
        redirect("/login", reload=True)


