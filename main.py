import streamlit as st

# Title
st.title("🌍 Unit Converter")

# Dictionary for conversion factors
conversion_factors = {
    "Length": {
        "Kilometers": {"Miles": 1 / 1.609, "Meters": 1000},
        "Miles": {"Kilometers": 1.609, "Meters": 1609},
        "Meters": {"Kilometers": 1 / 1000, "Feet": 3.281},
        "Feet": {"Meters": 1 / 3.281}
    },
    "Weight": {
        "Kilograms": {"Pounds": 2.20462, "Grams": 1000},
        "Pounds": {"Kilograms": 1 / 2.20462, "Ounces": 16},
        "Grams": {"Kilograms": 1 / 1000},
        "Ounces": {"Pounds": 1 / 16}
    },
    "Volume": {
        "Liters": {"Gallons": 0.264172, "Milliliters": 1000},
        "Gallons": {"Liters": 1 / 0.264172},
        "Milliliters": {"Liters": 1 / 1000}
    },
    "Temperature": {
        "Celsius": {"Fahrenheit": lambda x: x * 9/5 + 32, "Kelvin": lambda x: x + 273.15},
        "Fahrenheit": {"Celsius": lambda x: (x - 32) * 5/9, "Kelvin": lambda x: (x - 32) * 5/9 + 273.15},
        "Kelvin": {"Celsius": lambda x: x - 273.15, "Fahrenheit": lambda x: (x - 273.15) * 9/5 + 32}
    }
}

# User selects category
category = st.selectbox("Select a category:", list(conversion_factors.keys()))

# User inputs "From" and "To" units
from_unit = st.selectbox("Convert from:", list(conversion_factors[category].keys()))
to_unit = st.selectbox("Convert to:", list(conversion_factors[category][from_unit].keys()))

# User enters value to convert
value = st.number_input(f"Enter value in {from_unit}:", step=0.01, format="%.2f")

# Convert button
if st.button("Convert"):
    conversion = conversion_factors[category][from_unit][to_unit]
    result = conversion(value) if callable(conversion) else value * conversion
    st.success(f"Converted Value: {round(result, 4)} {to_unit}")

# Footer
st.markdown("---")
st.write("👨‍💻 Created with ❤️ by **Ismail Ahmed Shah**")
