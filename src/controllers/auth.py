from src.models.database import database
from src.models.cookie import Cookie
from hashlib import sha256

import streamlit as st 

def login(mail, mdp):
    db = database()
    mdp = sha256(mdp.encode(encoding="utf-32")).hexdigest()

    res = db.execute(f"SELECT * FROM users WHERE mail='{mail}' AND  password='{mdp}'").fetchone()
    
    if res != None: # si notre requete et non null
        c = Cookie("data.json") 
        c.update({"mail" : res[1],"uid": res[0]})
        return True
    else:
        return False


def signin (mail,motdepasse):
    db = database()
    motdepasse = sha256(motdepasse.encode(encoding="utf-32")).hexdigest()
    db.execute(f"Insert into users (mail, password) values('{mail}', '{motdepasse}')")
    db.commit()


def logout():
    c = Cookie("data.json")
    c.clean()