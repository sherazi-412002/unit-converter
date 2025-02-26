import streamlit as st
from components.header import render_header
from components.sidebar import render_sidebar
from components.converter_ui import render_converter
import config

def main():
    # Set page config
    st.set_page_config(
        page_title="Unit Converter App",
        page_icon="🔄",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Load custom CSS
    with open("styles/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    # Render header
    render_header()
    
    # Render sidebar
    selected_category = render_sidebar()
    
    # Render converter
    render_converter(selected_category)

if __name__ == "__main__":
    main()