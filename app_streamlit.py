import streamlit as st
from app.cesar import chiffrement_cesar, dechiffrement_cesar

# Titre de l'application
st.title("Chiffrement César")

# Saisie du texte
texte = st.text_area("Entrez le texte à chiffrer ou déchiffrer", value="")

# Saisie du décalage
decalage = st.slider("Choisissez le décalage", min_value=1, max_value=25, value=3)

# Choix entre chiffrer ou déchiffrer
choix = st.radio("Voulez-vous chiffrer ou déchiffrer ?", ("Chiffrer", "Déchiffrer"))

# Ajouter du style à l'interface
st.markdown(
    """
    <style>
    .stButton button {
        background-color: #FF5733;
        color: white;
        border-radius: 10px;
        font-size: 16px;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Bouton pour lancer l'opération
if st.button("Exécuter"):
    if choix == "Chiffrer":
        resultat = chiffrement_cesar(texte, decalage)
        st.success(f"Texte chiffré : {resultat}")
    else:
        resultat = dechiffrement_cesar(texte, decalage)
        st.success(f"Texte déchiffré : {resultat}")
    
    # Option de téléchargement du fichier texte
    st.download_button(
        label="Télécharger le résultat",
        data=resultat,
        file_name="resultat_cesar.txt",
        mime="text/plain"
    )

# Footer
st.text("Chiffrement César avec gestion des majuscules, minuscules, espaces et ponctuation.")