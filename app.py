import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
from acc import accueil
from photos import photos

st.set_page_config(
    page_title="Fingy album",
    page_icon="🖕",
    layout="wide",
)

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

# Initialiser l'authentification avec les informations d'identification
auth = stauth.Authenticate(credentials=lesDonneesDesComptes, cookie_name='cookie_session', key='secret_key')
authentication_status = auth.login()


# Affichage basé sur l'état d'authentification
if st.session_state["authentication_status"]:
    with st.sidebar:
        auth.logout("Déconnexion")
        st.write(f'Bienvenue *{st.session_state["name"]}*')
        selection = option_menu(
            menu_title=None,
            options=["👋 Accueil", "👉 Photos"]
        )
    if selection == "👋 Accueil":
        accueil()
    elif selection == "👉 Photos":
        photos()

elif st.session_state["authentication_status"] is False:
    st.error("Le nom d'utilisateur ou le mot de passe est incorrect.")
else:
    st.warning("Les champs username et mot de passe doivent être remplis.")