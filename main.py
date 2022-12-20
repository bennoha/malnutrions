import streamlit as st
from src.vues import login,home,objectif ,dataset,analyse,conclusions
from src.models.cookie import Cookie 
from src.router import redirect , get_route
import utils as utl
from src.controllers.auth import logout
from src.router import redirect
st.set_page_config( page_title='Navbar sample')
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()


def navigation():
    route = get_route()

    c = Cookie("data.json") # controlle du cookie 
    Valuecookie = dict(c.read())# transformer le cookie en dict 


    # la on force la connection de l'utulisateur 

    if Valuecookie["uid"] == None  and route !="/login":
        redirect("/login", reload=True)


    # la c'est notre systeme de route 

    if route =="/login": # renvois vers une vue login 
        if Valuecookie["uid"] != None: # dans le cas ou le cookie est pas vide -> connecté
             redirect("/home", reload=True) # redirige vers home 

        else: # -> pas connecté 

            login.load_view() # la on charge la vue login 


    elif route == "/home": # on renvois vers la vue home 
        home.load_view() # on recharge la vue home 

    elif route == "/objectif":# on renvois vers la vue objectif"
        objectif.load_view() #on recharge la vue objectif

    elif route =="/dataset":# on renvois vers la vue dataset
        dataset.load_view()#on recharge la vue dataset

    elif route =="/analyse":#on renvois vers la vue analyse
        analyse.load_view()#on recharge la vue analyse

    elif route == "/conclusions":#on renvois vers la vue conclusions
        conclusions.load_view()#on recharge la vue conclusions

    elif route == "/logout":
        logout()
        redirect("/login", reload=True)





    else:
        redirect("/login", reload=True)
        login.load_view()
        #navigation()
navigation()



