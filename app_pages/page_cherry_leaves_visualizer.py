import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random


def page_cherry_leaves_visualizer_body():
    st.write("### Cherry Leaves Visualizer")
    st.info(
        f"The customer is interested in having a study that visually "
        f"differentiates a cherry leaf that is healthy from one that contains "
        f"powdery mildew.")

    version = 'v1'
    if st.checkbox("Differences between average and variability cherry leaves images"):

        avg_infected = plt.imread(
            f"outputs/{version}/avg_var_powdery_mildew.png")
        avg_healthy = plt.imread(
            f"outputs/{version}/avg_var_healthy.png")

        st.warning(
            f"We can see that the average and variability images do not "
            f"demonstrate patterns where we could differentiate one from "
            f"another.")

        st.image(avg_infected,
                 caption='Cherry Leaf Infected with Powdery Mildew - Average and Variability')
        st.image(avg_healthy,
                 caption='Healthy Cherry Leaf - Average and Variability')
        st.write("---")

    if st.checkbox("Differences between average infected and average healthy cherry leaves images"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

        st.warning(
            f"The average infected cherry leaf image demonstrates white, "
            f"milky, or light gray spots, which differentiate it from "
            f"the average healthy cherry leaf image.")
        st.image(diff_between_avgs,
                 caption='Differences between average healthy and infected leaves')

    if st.checkbox("Image Montage"):
        st.write("To refresh the montage, click on the 'Create Montage' button")
        my_data_dir = 'inputs/cherry_leaves_dataset/cherry_leaves_images'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(
            label="Select label", options=labels, index=0)
        if st.button("Create Montage"):
            image_montage(dir_path=my_data_dir + '/validation',
                          label_to_display=label_to_display,
                          nrows=8, ncols=3, figsize=(10, 25))
        st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    if label_to_display in labels:

        # checks if your montage space is greater than subset size
        images_list = os.listdir(dir_path+'/' + label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return

        # create list of axes indices based on nrows and ncols
        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        # create a figure and display images
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows*ncols):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(
                f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)

    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")
