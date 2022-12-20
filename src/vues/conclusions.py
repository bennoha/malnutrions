import streamlit as st
from src.router import redirect 

def load_view():

    st.markdown("**Conclusions**")

    st.markdown("-la crise financiére et économique de 2008   a eu des effets plus que grave  sur le plan de la malnutritions dans tout les pays du monde mais plus particilierement les pays les plus pauvres et les moins développés")
    st.markdown("-les classes sociales a faible et a moyen revenu sont ples plus touchés par la malnutrions car la crise a causé une réduction du puvoir d'achat donc les classes econmique les plus modestes se sont retrouvées obliger de modifier leurs abitudes et leurs dépenses alimantaires vers des aliments avec un prix plus attractive mais avec un rapport nutritifs faible et la réductions voir la supressions des aliments plus couteux tel que les  viandes et les produit laitiers")
    st.markdown("-désormais la mal nutrions,l'amegrissement severe,le retard de croissance chez l'enfant,l'excés pondéral sont associées dans un grand nombres de pays ")
    if st.button("Conclusions"):
        redirect("/login", reload=True)
