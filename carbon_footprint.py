import pandas as pd

df = pd.read_csv("carbon-intensity-electricity.csv")
df = df.drop(columns=["Code","Year","Carbon intensity of electricity per kWh (Original Year)"])
print(df.head())

emission_dict = {
    row["Entity"]: row["Carbon intensity of electricity per kWh"] / 1000
    for _, row in df.iterrows()
}

# Fixed factors that don't vary much by country
OTHER_FACTORS = {
    "petrol": 2.31,
    "diesel": 2.68,
    "natural gas": 0.185,
    "car": 0.21,
}

# Merge: give every country all factors
EMISSION_FACTORS = {
    country: {"electric": elec_factor, **OTHER_FACTORS}
    for country, elec_factor in emission_dict.items()
}
def calculate_footprint(country, category, variable):
    factors = EMISSION_FACTORS.get(country, {})
    factor = factors.get(category, 0)
    return factor * variable