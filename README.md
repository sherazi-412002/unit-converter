
## Project 01
Created by: Syed Soaib Sherazi

## Description
A modern, Google-inspired unit converter built with Python and Streamlit. This application provides a clean, intuitive interface for converting between various units across multiple categories.

## Features
- Sleek, Google-inspired UI with responsive design
- Multiple conversion categories:
  - Length 📏
  - Mass ⚖️
  - Temperature 🌡️
  - Volume 🧪
  - Area 📐
  - Time ⏱️
  - Speed 🚀
  - Data 💾
  - Pressure 🔄
  - Energy ⚡
  - Currency 💰
- Interactive elements with animations
- Common comparisons for selected categories
- Detailed conversion formulas
- Mobile-friendly design

## Project Structure
```
project/
├── main.py             # Main application entry point
├── config.py           # Configuration and constants
├── utils.py            # Utility functions
├── converters/         # Converter modules
│   ├── __init__.py     # Makes directory a package
│   ├── length.py       # Length conversion logic
│   ├── mass.py         # Mass conversion logic
│   ├── temperature.py  # Temperature conversion logic
│   ├── volume.py       # Volume conversion logic
│   ├── area.py         # Area conversion logic
│   ├── time.py         # Time conversion logic
│   ├── speed.py        # Speed conversion logic
│   ├── data.py         # Data storage conversion logic
│   ├── pressure.py     # Pressure conversion logic
│   ├── energy.py       # Energy conversion logic
│   └── currency.py     # Currency conversion logic
├── components/         # UI components
│   ├── __init__.py     # Makes directory a package
│   ├── header.py       # Header component
│   ├── sidebar.py      # Sidebar component
│   └── converter_ui.py # Converter UI component
└── styles/             # CSS styling
    └── style.css       # Custom CSS
```

## Prerequisites
- Python 3.12.2
- Streamlit

## Installation
1. Clone this repository or download the source code
2. Install required packages:
```bash
pip install streamlit
```

## Running the Application
Navigate to the project directory and run:
```bash
streamlit run main.py
```

The application will start and automatically open in your default web browser.

## Customization
- Modify the color scheme in `config.py`
- Add new unit categories by creating new converter modules
- Customize the UI styling in `styles/style.css`

## License
This project is open source and available under the MIT License.