import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Project Summary")

    st.info(
        f"**General Information**\n\n"
        f"Powdery mildew is a fungal disease that affects a wide range of "
        f"plants. One of these plants is the cherry tree. The manual "
        f"detection of powdery mildew in cherry trees, which is done by "
        f"examining the leaves with the naked eye, is not a feasible method "
        f"because the total number of the cherry trees is huge.\n\n"
        f"The practical method to achieve this is implementing a machine "
        f"learning program that examines a cherry leaf image and immediately "
        f"determines whether it is healthy or infected with powdery mildew.\n\n"
        f"**Project Dataset**\n\n"
        f"Cherry leaf images that belong to **Farmy & Foods**.")

    st.write(
        f"* For more information about this project, plesae visit: "
        f"[Project repository](https://github.com/Majdi-Aref/mildew-detector).")

    st.success(
        f"This project handles two business requirements:\n"
        f"* 1 - The customer is interested in conducting a study to visually "
        f"differentiate a cherry leaf that is healthy from one that contains "
        f"powdery mildew.\n"
        f"* 2 - The customer is interested in predicting if a cherry "
        f"leaf is healthy or contains powdery mildew."
    )
