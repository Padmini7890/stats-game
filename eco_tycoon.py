import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt

# Initialize session state variables
if 'economy' not in st.session_state:
    st.session_state.economy = 50
if 'environment' not in st.session_state:
    st.session_state.environment = 50
if 'happiness' not in st.session_state:
    st.session_state.happiness = 50
if 'turns' not in st.session_state:
    st.session_state.turns = 0

st.title("🌱 Eco Tycoon: The Data-Driven City")
st.write("Manage your city sustainably and survive as long as possible!")

# Decision buttons
def make_decision(decision):
    impact = {
        "Invest in Solar Energy": {"economy": -5, "environment": +15, "happiness": +5},
        "Subsidize Public Transport": {"economy": -10, "environment": +10, "happiness": +10},
        "Increase Industrial Production": {"economy": +15, "environment": -20, "happiness": -5},
        "Ban Plastic Usage": {"economy": -5, "environment": +10, "happiness": -2},
        "Build More Parks": {"economy": -8, "environment": +12, "happiness": +15},
        "Relax Pollution Laws": {"economy": +10, "environment": -15, "happiness": -10},
    }
    
    if decision in impact:
        for key in impact[decision]:
            st.session_state[key] += impact[decision][key]
        st.session_state.turns += 1

# Display choices
st.write("### Make a Decision:")
choices = ["Invest in Solar Energy", "Subsidize Public Transport", "Increase Industrial Production", "Ban Plastic Usage", "Build More Parks", "Relax Pollution Laws"]
for choice in choices:
    if st.button(choice):
        make_decision(choice)

# Check win/loss conditions
if st.session_state.environment <= 0:
    st.error("🌍 Your city became too polluted! Game Over!")
elif st.session_state.economy <= 0:
    st.error("💰 Your economy collapsed! Game Over!")
elif st.session_state.happiness <= 0:
    st.error("😢 Citizens are too unhappy! Game Over!")
else:
    # Display stats
    st.write("### City Stats:")
    stats_df = pd.DataFrame({
        "Category": ["Economy", "Environment", "Happiness"],
        "Score": [st.session_state.economy, st.session_state.environment, st.session_state.happiness]
    })
    st.bar_chart(stats_df.set_index("Category"))
    
    st.write(f"**Turns Survived:** {st.session_state.turns}")
