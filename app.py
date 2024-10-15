import streamlit as st
import os
from textsummarizer.pipeline.prediction import PredictionPipeline

# Title and Introduction
st.title("Text Summarization App")
st.write("This app performs text summarization using a pre-trained model.")

# Add an input text box for prediction
text = st.text_area("Enter Text for Summarization", "What is Text Summarization?")

# Training section
if st.button("Train Model"):
    st.write("Training started...")
    try:
        # Simulate the training process
        os.system("python main.py")
        st.success("Training successful!")
    except Exception as e:
        st.error(f"Error occurred during training: {e}")

# Prediction section
if st.button("Summarize Text"):
    if text:
        st.write("Summarizing the text...")
        try:
            # Prediction pipeline instance
            obj = PredictionPipeline()
            summarized_text = obj.predict(text)
            st.write("Summarized Text:")
            st.success(summarized_text)
        except Exception as e:
            st.error(f"Error occurred during summarization: {e}")
    else:
        st.warning("Please enter some text for summarization.")

