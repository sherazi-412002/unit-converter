import streamlit as st
import config
from utils import create_gradient_text

def render_header():
    """Render the application header"""
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(
            f"""
            <h1 class="app-title">
                <span class="emoji-pop">🔄</span> {config.APP_TITLE}
            </h1>
            <p class="app-description">{config.APP_DESCRIPTION}</p>
            """, 
            unsafe_allow_html=True
        )
    
    with col2:
        # Google-inspired logo
        colors = [config.COLORS["primary"], config.COLORS["secondary"], 
                  config.COLORS["accent1"], config.COLORS["accent2"]]
        logo_html = f"""
        <div class="google-logo">
            <span style="color:{colors[0]}">U</span>
            <span style="color:{colors[1]}">n</span>
            <span style="color:{colors[2]}">i</span>
            <span style="color:{colors[3]}">t</span>
        </div>
        """
        st.markdown(logo_html, unsafe_allow_html=True)
    
    # Add divider
    st.markdown("<hr class='fancy-divider'>", unsafe_allow_html=True)