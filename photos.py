import streamlit as st

def photos():
    st.markdown("<h1 style='text-align: center; color: white;'>Bienvenue sur mon album photo</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<h3 style='text-align: center; color: white;'>Fingy à la forêt</h3>", unsafe_allow_html=True)
        st.image("/Leonardo_Phoenix_A_gritty_highcontrast_image_of_a_lone_middle_3.jpg")

    with col2:
        st.markdown("<h3 style='text-align: center; color: white;'>Fingy à la plage</h3>", unsafe_allow_html=True)
        st.image("/Leonardo_Phoenix_A_solitary_hand_with_a_prominent_middle_finge_0.jpg")

    with col3:
        st.markdown("<h3 style='text-align: center; color: white;'>Fingy à la montagne</h3>", unsafe_allow_html=True)
        st.image("/Leonardo_Phoenix_updatedpromptA_dramatic_highcontrast_image_fe_3.jpg")