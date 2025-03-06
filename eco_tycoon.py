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
if 'population' not in st.session_state:
    st.session_state.population = 1000
if 'turns' not in st.session_state:
    st.session_state.turns = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'events' not in st.session_state:
    st.session_state.events = ""

st.title("🌱 Eco Tycoon: The Data-Driven City")
st.write("Manage your city sustainably and survive as long as possible!")

# Reset game function
def reset_game():
    st.session_state.economy = 50
    st.session_state.environment = 50
    st.session_state.happiness = 50
    st.session_state.population = 1000
    st.session_state.turns = 0
    st.session_state.game_over = False
    st.session_state.events = ""

# Random event generator
def random_event():
    events = [
        ("🌍 Climate Crisis! Pollution levels rise drastically.", {"environment": -15}),
        ("💰 Economic Boom! Your city's economy flourishes.", {"economy": +15}),
        ("🌿 Green Revolution! Citizens embrace sustainability.", {"environment": +10, "happiness": +5}),
        ("🔥 Factory Fire! Industrial production is affected.", {"economy": -10, "happiness": -5}),
        ("💡 Energy Breakthrough! Renewable energy efficiency increases.", {"economy": +5, "environment": +10}),
        ("🌊 Flood Disaster! Major damage to infrastructure.", {"economy": -12, "happiness": -8, "environment": -10}),
        ("📈 Tax Reform! Government introduces new policies.", {"economy": +10, "happiness": -5})
    ]
    event, effects = random.choice(events)
    st.session_state.events = event
    for key, value in effects.items():
        st.session_state[key] += value

# Decision buttons
def make_decision(decision):
    if st.session_state.game_over:
        return
    
    impact = {
        "Invest in Solar Energy": {"economy": -5, "environment": +15, "happiness": +5},
        "Subsidize Public Transport": {"economy": -10, "environment": +10, "happiness": +10},
        "Increase Industrial Production": {"economy": +15, "environment": -20, "happiness": -5},
        "Ban Plastic Usage": {"economy": -5, "environment": +10, "happiness": -2},
        "Build More Parks": {"economy": -8, "environment": +12, "happiness": +15},
        "Relax Pollution Laws": {"economy": +10, "environment": -15, "happiness": -10},
        "Invest in Green Technology": {"economy": -12, "environment": +20, "happiness": +8},
        "Impose Higher Taxes": {"economy": +15, "happiness": -10},
        "Disaster Relief Fund": {"economy": -10, "happiness": +10},
        "Urban Expansion": {"economy": +10, "environment": -10, "population": +200},
    }
    
    if decision in impact:
        for key in impact[decision]:
            st.session_state[key] += impact[decision][key]
        st.session_state.turns += 1
        
        # Random event after every turn
        if random.random() < 0.5:  # 50% chance of an event occurring
            random_event()
    
    # Check win/loss conditions
    if st.session_state.environment <= 0:
        st.session_state.game_over = True
        st.error("🌍 Your city became too polluted! Game Over!")
    elif st.session_state.economy <= 0:
        st.session_state.game_over = True
        st.error("💰 Your economy collapsed! Game Over!")
    elif st.session_state.happiness <= 0:
        st.session_state.game_over = True
        st.error("😢 Citizens are too unhappy! Game Over!")
    elif st.session_state.population <= 500:
        st.session_state.game_over = True
        st.error("🏙️ Your city population declined too much! Game Over!")

# Display choices
if not st.session_state.game_over:
    st.write("### Make a Decision:")
    choices = [
        "Invest in Solar Energy", "Subsidize Public Transport", "Increase Industrial Production", "Ban Plastic Usage", "Build More Parks", "Relax Pollution Laws",
        "Invest in Green Technology", "Impose Higher Taxes", "Disaster Relief Fund", "Urban Expansion"
    ]
    for choice in choices:
        if st.button(choice):
            make_decision(choice)

# Display random event
if st.session_state.events:
    st.warning(st.session_state.events)

# Display stats
st.write("### City Stats:")
stats_df = pd.DataFrame({
    "Category": ["Economy", "Environment", "Happiness", "Population"],
    "Score": [st.session_state.economy, st.session_state.environment, st.session_state.happiness, st.session_state.population]
})
st.bar_chart(stats_df.set_index("Category"))

st.write(f"**Turns Survived:** {st.session_state.turns}")

# Show restart button if game over
if st.session_state.game_over:
    if st.button("🔄 Restart Game"):
        reset_game()
