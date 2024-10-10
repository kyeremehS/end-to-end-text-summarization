import streamlit as st
from transformers import PegasusTokenizer, PegasusForConditionalGeneration

# Load model and tokenizer
@st.cache_resource
def load_model():
    tokenizer = PegasusTokenizer.from_pretrained('google/pegasus-cnn_dailymail')
    model = PegasusForConditionalGeneration.from_pretrained('google/pegasus-cnn_dailymail')
    return tokenizer, model

tokenizer, model = load_model()

# Summarization function
def summarize_text(text):
    tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")
    summary_ids = model.generate(tokens['input_ids'], max_length=150, num_beams=4, length_penalty=2.0, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Streamlit app
def main():
    st.title("Text Summarization App")
    st.write("This app summarizes text using Pegasus transformer model.")
    
    # Input text area
    input_text = st.text_area("Enter the text you want to summarize", height=200)

    # Summarize button
    if st.button("Summarize"):
        if input_text:
            with st.spinner("Summarizing..."):
                summary = summarize_text(input_text)
                st.subheader("Summary")
                st.write(summary)
        else:
            st.error("Please enter some text to summarize.")

if __name__ == "__main__":
    main()
