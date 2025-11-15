import google.generativeai as palm
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')
if api_key is None:
    raise Exception('API_KEY not found...')

palm.configure(api_key=api_key)

def summarize_article(model, prompt, temperature, max_output_tokens):
    completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=temperature,
    max_output_tokens=max_output_tokens,
)
    return completion

def app():
    prompt_objective = "Objective: Summarize the following article."
    st.title("Enter Article Text or URL to Summarize")
    article_text = st.text_area("Article Text")
    temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, step=0.1, value=0.6)
    max_output_tokens = st.slider("Max Output Tokens", min_value=100, max_value=2000, step=100, value=800)
    model_options = ["models/text-bison-001"]
    MODEL = st.selectbox("Model", model_options)
    prompt = prompt_objective + "\n" + article_text
    if st.button("Summarize"):
        res = summarize_article(MODEL, prompt, temperature, max_output_tokens)
        summary = res.candidates[0]['output']
        st.write("Summary:")
        st.write(summary)

if __name__ == "__main__":
    app()
