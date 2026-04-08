import streamlit as st
from carbon_footprint import calculate_footprint,EMISSION_FACTORS
import pandas as pd
import plotly.express as px

st.title("Carbon Emission Calculator")
st.sidebar.title("Selections")
country = st.sidebar.selectbox("Country", list(EMISSION_FACTORS.keys()))

kwh = st.sidebar.number_input("Electricity (kWh)")
fuel = st.sidebar.number_input("Fuel (liters)")
gas = st.sidebar.number_input("Natural Gas(kwh)")
transport = st.sidebar.number_input("Car(km)")


if st.button("Calculate"):
    elec_footprint = calculate_footprint(country,"electric",kwh)
    fuel_footprint = calculate_footprint(country,"petrol",fuel)
    gas_footprint = calculate_footprint(country,"natural gas",gas)
    trans_footprint = calculate_footprint(country,"car", transport)
    total_footprint = elec_footprint + fuel_footprint + gas_footprint + trans_footprint
    
    breakdown = {
    "Category": ["Electricity", "Fuel", "Natural Gas", "Car"],
    "kg CO2": [elec_footprint, fuel_footprint, gas_footprint, trans_footprint]
    }
    df = pd.DataFrame(breakdown)
    fig = px.bar(
    df,
    x="Category",
    y="kg CO2",
    title="Emissions Breakdown",
    color="Category"
    )

    st.write(f"Emissions: {total_footprint:.2f} kg CO2")
    st.plotly_chart(fig)