
def format_number(number):
    """Format number to be more readable"""
    if abs(number) < 0.000001 or abs(number) > 1000000:
        return f"{number:.6e}"
    elif abs(number) < 0.001:
        return f"{number:.8f}".rstrip('0').rstrip('.') if '.' in f"{number:.8f}" else f"{number:.8f}"
    elif abs(number) < 0.1:
        return f"{number:.6f}".rstrip('0').rstrip('.') if '.' in f"{number:.6f}" else f"{number:.6f}"
    else:
        return f"{number:.4f}".rstrip('0').rstrip('.') if '.' in f"{number:.4f}" else f"{number:.4f}"

def get_conversion_hint(from_unit, to_unit, value, result):
    """Generate a helpful conversion hint"""
    if value == 0:
        return ""
    
    ratio = result / value if value != 0 else 0
    
    if 0.8 < ratio < 1.2:
        return f"💡 {from_unit} and {to_unit} are similar in magnitude."
    elif ratio > 1:
        return f"💡 {to_unit} is larger than {from_unit} (× {format_number(ratio)})."
    else:
        return f"💡 {to_unit} is smaller than {from_unit} (× {format_number(ratio)})."

def apply_animation(element, animation_class):
    """Apply CSS animation to an element"""
    return f"""
    <div class="{animation_class}">
        {element}
    </div>
    """

def create_gradient_text(text, color1, color2):
    """Create text with gradient effect"""
    return f"""
    <div class="gradient-text" style="background: linear-gradient(90deg, {color1}, {color2});">
        {text}
    </div>
    """