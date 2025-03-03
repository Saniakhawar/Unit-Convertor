import streamlit as st

st.title("🌎 Unit Converter App")
st.markdown("### Convert Length, Weight, and Time Instantly")
st.write("Welcome! Select a category, enter a value, and choose a unit to convert it.")

# Select Category
category = st.selectbox("Select a category", ["Length", "Weight", "Time"])

# Define unit conversion options
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["kilometers to miles", "miles to kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["kilograms to pounds", "pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("⏳ Select Conversion", [
        "seconds to minutes", "minutes to seconds",
        "hours to seconds", "seconds to hours",
        "hours to days", "days to hours"
    ])

# Get user input for value
value = st.number_input("Enter the value to convert", min_value=0.0, format="%.6f")

# Conversion function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "kilometers to miles":
            return value * 0.621371
        elif unit == "miles to kilometers":
            return value / 0.621371
    elif category == "Weight":
        if unit == "kilograms to pounds":
            return value * 2.20462
        elif unit == "pounds to kilograms":
            return value / 2.20462
    elif category == "Time":
        if unit == "seconds to minutes":
            return value / 60
        elif unit == "minutes to seconds":
            return value * 60
        elif unit == "hours to seconds":
            return value * 3600
        elif unit == "seconds to hours":
            return value / 3600
        elif unit == "hours to days":
            return value / 24
        elif unit == "days to hours":
            return value * 24
    return None

# Perform conversion when button is clicked
if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"The result is {result:.6f}")
    else:
        st.error("Invalid conversion")
