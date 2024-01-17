import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"Cherry leaves that are infected with powdery mildew have distinctive "
        f"features that differentiate them from healthy ones. \n\n"
        f"The infected cherry leaves reveal white, milky, or light "
        f"gray spots. \n\n"
        f"Our machine learning program can efficiently detect these "
        f"distinctive features and differentiate between healthy and "
        f"infected cherry leaves."
    )
