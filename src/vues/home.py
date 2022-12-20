import streamlit as st
from src.controllers.auth import logout
from src.router import redirect
def load_view():
    st.title("home")
    st.markdown("bienvenu sur le site")


    st.markdown("**le but de la création de ce site web**:")
    st.markdown("mettre en pratique et appliquer tout ce qu'on a appris tout au long de cette formation")

    st.markdown("**nous avons utuliser PYTHON comme langage de programmation**:")
    st.markdown("**le choix de ce langage:**")
    st.markdown("-simple et facile,il facile a apprendre et a coder c'est pourquoi lorsque les gens choisissent python,ils ont du mal a s'adapter aux autres langages plus verbeux comme Java")
    st.markdown("-Moins de code,presque totes les taches effectéesen python néecessitent moins de codage lorsque la meme tache est effectuée dans d'autres langues")
    st.markdown("-python est totalement gratuit")
    st.markdown("-Bibliothéques étendues")
    if st.button("home"):
        logout()
        redirect("login" , reload=True)

   



