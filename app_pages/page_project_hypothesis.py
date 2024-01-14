import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"Cherry leaves infected with powdery mildew have distinctive "
        f"features that differentiate them from healthy ones."
        f"The infected ones reveal white or light gray spots."
        f"Our machine learning program can efficiently detect these "
        f"distinctive features and differentiate between healthy and "
        f"infected cherry leaves."
    )
