import streamlit as st
import config
from converters import get_converter
from utils import format_number, get_conversion_hint

def render_converter(category):
    """Render the converter UI for the selected category"""
    
    # Get the units for the selected category
    units = config.UNITS[category]
    
    # Get the converter module for the selected category
    converter = get_converter(category)
    
    st.markdown(
        f"""
        <div class="converter-header">
            <h2>{config.CATEGORIES[category]} {category} Converter</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Create two columns for the converter
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='unit-card source-unit'>", unsafe_allow_html=True)
        st.markdown(f"<h3>From {config.CATEGORIES[category]}</h3>", unsafe_allow_html=True)
        
        # Value input
        value = st.number_input(
            "Enter value",
            value=1.0,
            step=1.0,
            format="%.2f",
            label_visibility="collapsed",
            key="input_value"
        )
        
        # From unit selection
        from_unit = st.selectbox(
            "From Unit",
            units,
            index=0,
            label_visibility="collapsed",
            key="from_unit"
        )
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='unit-card target-unit'>", unsafe_allow_html=True)
        st.markdown(f"<h3>To {config.CATEGORIES[category]}</h3>", unsafe_allow_html=True)
        
        # To unit selection
        to_unit = st.selectbox(
            "To Unit",
            units,
            index=1 if len(units) > 1 else 0,
            label_visibility="collapsed",
            key="to_unit"
        )
        
        # Perform conversion
        try:
            result = converter.convert(value, from_unit, to_unit)
            formatted_result = format_number(result)
            
            # Display result with animation
            st.markdown(
                f"""
                <div class="result-container">
                    <div class="result-value">{formatted_result}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        except Exception as e:
            st.error(f"Conversion error: {str(e)}")
            formatted_result = "Error"
            result = 0
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Show conversion hint
    hint = get_conversion_hint(from_unit, to_unit, value, result)
    if hint:
        st.markdown(f"<div class='conversion-hint'>{hint}</div>", unsafe_allow_html=True)
    
    # Formula display
    st.markdown(
        f"""
        <div class="formula-box">
            <span class="formula-label">✓ Formula:</span>
            <span class="formula-value">{value} {from_unit} = {formatted_result} {to_unit}</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    
#     # Add common values comparison
#     if category == "Length" and result != 0:
#         show_common_comparisons(value, from_unit, result, to_unit)
#     elif category == "Mass" and result != 0:
#         show_mass_comparisons(value, from_unit, result, to_unit)
#     elif category == "Temperature" and result != 0:
#         show_temperature_comparisons(from_unit, to_unit, value, result)

# def show_common_comparisons(value, from_unit, result, to_unit):
#     """Show common comparisons for length values"""
#     st.markdown("<div class='comparison-section'>", unsafe_allow_html=True)
#     st.markdown("<h4>📏 Common Comparisons</h4>", unsafe_allow_html=True)
    
#     comparisons = [
#         {"name": "Width of human hair", "value": 0.1, "unit": "Millimeter"},
#         {"name": "Length of ant", "value": 5, "unit": "Millimeter"},
#         {"name": "Credit card width", "value": 8.5, "unit": "Centimeter"},
#         {"name": "Average height of human", "value": 1.7, "unit": "Meter"},
#         {"name": "Empire State Building height", "value": 443, "unit": "Meter"}
#     ]
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         for comp in comparisons[:3]:
#             converter = get_converter("Length")
#             compared_value = converter.convert(comp["value"], comp["unit"], to_unit)
#             ratio = result / compared_value if compared_value != 0 else 0
            
#             st.markdown(
#                 f"""
#                 <div class="comparison-item">
#                     <div class="comparison-name">{comp["name"]}</div>
#                     <div class="comparison-value">
#                         {format_number(ratio)}× {comp["name"]}
#                     </div>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )
    
#     with col2:
#         for comp in comparisons[3:]:
#             converter = get_converter("Length")
#             compared_value = converter.convert(comp["value"], comp["unit"], to_unit)
#             ratio = result / compared_value if compared_value != 0 else 0
            
#             st.markdown(
#                 f"""
#                 <div class="comparison-item">
#                     <div class="comparison-name">{comp["name"]}</div>
#                     <div class="comparison-value">
#                         {format_number(ratio)}× {comp["name"]}
#                     </div>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )
    
#     st.markdown("</div>", unsafe_allow_html=True)

# def show_mass_comparisons(value, from_unit, result, to_unit):
#     """Show common comparisons for mass values"""
#     st.markdown("<div class='comparison-section'>", unsafe_allow_html=True)
#     st.markdown("<h4>⚖️ Common Comparisons</h4>", unsafe_allow_html=True)
    
#     comparisons = [
#         {"name": "Paperclip", "value": 1, "unit": "Gram"},
#         {"name": "Smartphone", "value": 200, "unit": "Gram"},
#         {"name": "Laptop", "value": 2, "unit": "Kilogram"},
#         {"name": "Adult human", "value": 70, "unit": "Kilogram"},
#         {"name": "Car", "value": 1.5, "unit": "Metric Ton"}
#     ]
    
#     cols = st.columns(5)
    
#     for i, comp in enumerate(comparisons):
#         with cols[i]:
#             converter = get_converter("Mass")
#             compared_value = converter.convert(comp["value"], comp["unit"], to_unit)
#             ratio = result / compared_value if compared_value != 0 else 0
            
#             st.markdown(
#                 f"""
#                 <div class="comparison-item-small">
#                     <div class="comparison-name">{comp["name"]}</div>
#                     <div class="comparison-value">
#                         {format_number(ratio)}×
#                     </div>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )
    
#     st.markdown("</div>", unsafe_allow_html=True)

# def show_temperature_comparisons(from_unit, to_unit, value, result):
#     """Show temperature reference points"""
#     st.markdown("<div class='comparison-section'>", unsafe_allow_html=True)
#     st.markdown("<h4>🌡️ Temperature Reference Points</h4>", unsafe_allow_html=True)
    
#     references = [
#         {"name": "Freezing Point of Water", "celsius": 0},
#         {"name": "Room Temperature", "celsius": 20},
#         {"name": "Body Temperature", "celsius": 37},
#         {"name": "Boiling Point of Water", "celsius": 100}
#     ]
    
#     converter = get_converter("Temperature")
    
#     cols = st.columns(4)
    
#     for i, ref in enumerate(references):
#         with cols[i]:
#             # Convert reference from Celsius to the target unit
#             ref_in_target = converter.convert(ref["celsius"], "Celsius", to_unit)
            
#             # Determine if our result is close to this reference
#             is_close = abs(result - ref_in_target) < abs(ref_in_target * 0.1)
#             highlight_class = "temperature-highlight" if is_close else ""
            
#             st.markdown(
#                 f"""
#                 <div class="temperature-ref {highlight_class}">
#                     <div class="ref-name">{ref["name"]}</div>
#                     <div class="ref-value">{format_number(ref_in_target)} {to_unit}</div>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )
    
#     st.markdown("</div>", unsafe_allow_html=True)