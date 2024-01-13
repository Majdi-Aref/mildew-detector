import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_leaf_visualizer import page_leaf_visualizer_body
from app_pages.page_powdery_mildew_detection import page_powdery_mildew_detection_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_performance import page_ml_performance_metrics

# create an app instance
app = MultiPage(app_name="Mildew Detector")

# Add app pages
app.add_page("Project Summary", page_summary_body)
app.add_page("Cherry Leaf Visualiser", page_leaf_visualizer_body)
app.add_page("Powdery Mildew Detection", page_powdery_mildew_detection_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("ML Performance Metrics", page_ml_performance_metrics)

app.run()  # Run the app
