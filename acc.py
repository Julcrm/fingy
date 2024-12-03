import streamlit as st

def accueil():
    st.markdown("<h1 style='text-align: center; color: white;'>Bienvenue sur ma page </h1>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
            <img src="https://media1.tenor.com/m/RsGccAKKOcUAAAAd/middle-finger.gif" alt="Centered Image" style="max-width: 100%; height: auto;">
        </div>
        """,
        unsafe_allow_html=True
    )
