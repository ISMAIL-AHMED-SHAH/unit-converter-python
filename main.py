import streamlit as st

# Title
st.title("🌍 Unit Converter")

# Dictionary for conversions
conversions = {
    "Kilometers to Miles": lambda x: x / 1.609,
    "Miles to Kilometers": lambda x: x * 1.609,
    "Kilograms to Pounds": lambda x: x * 2.20462,
    "Pounds to Kilograms": lambda x: x / 2.20462,
    "Celsius to Fahrenheit": lambda x: x * 9/5 + 32,
    "Fahrenheit to Celsius": lambda x: (x - 32) * 5/9,
    "Inches to Centimeters": lambda x: x * 2.54,
    "Centimeters to Inches": lambda x: x / 2.54
}

# Dropdown for conversion type
conversion_type = st.selectbox("Select a conversion type:", list(conversions.keys()))

# User input for value
value = st.number_input("Enter value:", min_value=0.0, step=0.01, format="%.2f")

# Convert button
if st.button("Convert"):
    result = conversions[conversion_type](value)
    st.success(f"Converted Value: {round(result, 4)}")

# Footer
st.markdown("---")
st.write("👨‍💻 Created with ❤️ by **Ismail Ahmed Shah**")
