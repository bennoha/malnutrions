 
import streamlit as st
from src.controllers.auth import login
from src.router import redirect


def load_view():
   st.title("page de connexion")
   mail = st.text_input("mail")
   password = st.text_input("password", type="password")


   if st.button("se connecter"):
      if login(mail, password):
         st.text("vous etes connecter")
         redirect("/home", reload=True)
      
      else:
         st.text("Ereur de connexion")

   

