# import streamlit as st
# import config

# def render_sidebar():
#     """Render the sidebar with category selection"""
    
#     st.sidebar.markdown(
#         f"""
#         <div class="sidebar-header">
#             <h2>Categories <span class="emoji-pop">📚</span></h2>
#         </div>
#         """, 
#         unsafe_allow_html=True
#     )
    
#     # Create category selector
#     categories = list(config.CATEGORIES.keys())
    
#     # Use radio buttons with custom styling
#     cat_options = [f"{config.CATEGORIES[cat]} {cat}" for cat in categories]
    
#     selected_option = st.sidebar.radio(
#         "Select Category",
#         cat_options,
#         label_visibility="collapsed"
#     )
    
#     # Extract the category name without emoji
#     selected_category = selected_option.split(" ", 1)[1]
    
#     # Show information about selected category
#     st.sidebar.markdown(
#         f"""
#         <div class="selected-category">
#             <h3>{config.CATEGORIES[selected_category]} {selected_category}</h3>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
    
#     # Add a sidebar footer
#     st.sidebar.markdown(
#         """
#         <div class="sidebar-footer">
#             <p>Unit converter with modern interface</p>
#             <p>🔄 Google-style precision</p>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
    
#     return selected_category



import streamlit as st
import config

def render_sidebar():
    """Render the sidebar with category selection"""
    
    # Apply custom CSS for spacing and font size
    st.sidebar.markdown(
        """
        <style>
            div[role="radiogroup"] label {
                font-size: 3rem !important; 
                margin-bottom: 10px !important; 
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        f"""
        <div class="sidebar-header">
            <h2>Categories <span class="emoji-pop">📚</span></h2>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Create category selector
    categories = list(config.CATEGORIES.keys())
    
    # Use radio buttons with custom styling
    cat_options = [f"{config.CATEGORIES[cat]} {cat}" for cat in categories]
    
    selected_option = st.sidebar.radio(
        "Select Category",
        cat_options,
        label_visibility="collapsed",
        
    )
    
    # Extract the category name without emoji
    selected_category = selected_option.split(" ", 1)[1]
    
    # Show information about selected category
    st.sidebar.markdown(
        f"""
        <div class="selected-category">
            <h3>{config.CATEGORIES[selected_category]} {selected_category}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Add a sidebar footer
    st.sidebar.markdown(
        """
        <div class="sidebar-footer">
            <p class="creator-text">Created By Syed Soaib Sherazi</p>
            <p>🔄 Google-style precision</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    return selected_category
