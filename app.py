import streamlit as st
import pandas as pd


st.set_page_config(
    page_title = "🔄 Unit Converter",
    page_icon = "🔄",
    layout = "centered"
)

st.markdown(
    """
    <style>
        .main {
            padding: 2rem
        }
        .stButton > button {
            background-color: #ff4b4b;
            color: white;
            border-radius: 10px;
            padding: 0.5rem 2rem;
            border: none   
        }
        .stButton > button:hover {
            background-color: #ff6b6b;
        }
        .title {
            text-align: center;
            color: #1f1f1f
            font-size: 3rem;
            margin-bottom: 2rem;
        }
        .result {
            padding: 1rem;
            background-color: #f0f2f6;
            border-radius: 10px;
            font-size: 1.5rem;
            text-align: center;
            margin-top: 2rem;
            font-weight: bold;
            color: #1f1f1f;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            cursor: pointer;
        }
        .result:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
        }
    </style>
    """, unsafe_allow_html  =   True
)

st.markdown("<h1 class='title'>🔄 Unit Converter</h1>", unsafe_allow_html = True)

categories = {
    "Length 📏": {
        "units": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Inch", "Foot"],
        "emoji": "📏"
    },
    "Weight ⚖️": {
        "units": ["Kilogram", "Gram", "Miligram", "Pound", "Ounce"],
        "emoji": "⚖️"
    },
    "Temperature 🌡️": {
        "units": ["Celsius", "Fahrenheit", "Kelvin"],
        "emoji": "🌡️"
    },
    "Volume 💧": {
        "units": ["Liter", "Milliliter", "Gallon", "Cubic Meter", "Cubic Foot", "Cubic Inch"],
        "emoji": "💧"
    },
    "Time ⏰": {
        "units": ["Second", "Minute", "Hour", "Day", "Week", "Month", "Year"],
        "emoji": "⏰"
    },
    "Currency 💰": {
        "units": ["Dollar", "Euro", "Pound", "Rupee", "Yen", "Ruble", "PKR"],
        "emoji": "💰"
    },

}

def convert_length(value, from_unit, to_unit):
    meters = {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Inch": 0.0254,
        "Foot": 0.3048
    }
    return value * meters[from_unit] / meters[to_unit]

def convert_weight(value, from_unit, to_unit):
    grams = {
        "Kilogram": 1000,
        "Gram": 1,
        "Miligram": 0.001,
        "Pound": 453.592,
        "Ounce": 28.3495
    }
    return value * grams[from_unit] / grams[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        if to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        if to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        if to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32

def convert_volume(value, from_unit, to_unit):
    liters = {
        "Liter": 1,
        "Milliliter": 0.001,
        "Gallon": 3.78541,
        "Cubic Meter": 1,
        "Cubic Foot": 0.0283168,
        "Cubic Inch": 0.0000163871
    }
    return value * liters[from_unit] / liters[to_unit]

def convert_time(value, from_unit, to_unit):
    seconds = {
        "Second": 1,
        "Minute": 60,
        "Hour": 3600,
        "Day": 86400,
        "Week": 604800,
        "Month": 2629746,
        "Year": 31556952
    }
    return value * seconds[from_unit] / seconds[to_unit]

def convert_currency(value, from_unit, to_unit):
    dollars = {
        "Dollar": 1,
        "Euro": 0.85,
        "Pound": 0.72,
        "Rupee": 82.5,
        "Yen": 110.5,
        "Ruble": 75.5,
        "PKR": 200
    }
    return value * dollars[from_unit] / dollars[to_unit]


category = st.sidebar.selectbox(
    "Select Category",
    list(categories.keys())
)

col1, col2, col3 = st.columns(3)

with col1:
    value = st.number_input("Enter Value", value=0.0)

with col2:
    from_unit = st.selectbox("From Unit", categories[category]["units"])

with col3:
    to_unit = st.selectbox("To Unit", categories[category]["units"])


if st.button("Convert ✨"):
    result = None
    if category == "Length 📏":
        result = convert_length(value, from_unit, to_unit)
    elif category == "Weight ⚖️":
        result = convert_weight(value, from_unit, to_unit)
    elif category == "Temperature 🌡️":
        result = convert_temperature(value, from_unit, to_unit)
    elif category == "Volume 💧":
        result = convert_volume(value, from_unit, to_unit)
    elif category == "Time ⏰":
        result = convert_time(value, from_unit, to_unit)
    elif category == "Currency 💰":
        result = convert_currency(value, from_unit, to_unit)

    if result is not None:
        st.markdown(f"<div class='result'>{value} {from_unit} = {result: .4f} {to_unit}</div>", unsafe_allow_html = True)


st.markdown("---")
st.markdown("### 💫 Unit Converter Features:")
st.markdown("""
- 📏 Length Conversion
- ⚖️ Weight Conversion
- 🌡️ Temperature Conversion
- 💧 Volume Conversion
- ⏰ Time Conversion
- 💰 Currency Conversion
- 🎨 Beautiful UI
- 📱 Mobile Friendly Design
""")
