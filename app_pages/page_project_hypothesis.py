import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypotheses and their Validations")

    st.success(
        f"1. Cherry leaves that are infected with powdery mildew have "
        f"distinctive features that differentiate them from healthy ones. "
        f"The infected cherry leaves reveal white, milky, or light "
        f"gray spots. My machine learning program can efficiently "
        f"detect these distinctive features and differentiate between "
        f"healthy and infected cherry leaves. \n\n"
        f"2. My machine learning program can significantly accelerate "
        f"the cherry leaf examination process, which would save a business "
        f"huge amounts of time, effort, and money. This machine learning "
        f"program can execute an instantaneous prediction with an accuracy "
        f"of about 99%, which would save at least 90% of the time, effort, "
        f"and money needed to inspect the cherry leaves manually with the "
        f"naked eye. \n\n"
        f"3. Manual inspections of cherry leaves are prone to human errors, "
        f"such as overlooking infected cherry leaves, which can be reduced. "
        f"This image analysis program is less prone to these errors; "
        f"therefore, it can provide more accurate results. \n\n"
        f"4. Detection of early stages of powdery mildew infection in cherry "
        f"leaves would help a business to take action to control this disease "
        f"before it spreads to a large number of trees. This program is more "
        f"capable than humans in detecting signs of powdery mildew in cherry "
        f"leaves, which enables a business to adopt prevention and early "
        f"treatment measures."
    )
