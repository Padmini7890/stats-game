import streamlit as st
import random
from itertools import combinations

# Game Setup
TOTAL_CHESTS = 10
GOLDEN_CHESTS = 3  # Number of chests with gold

def reset_game():
    st.session_state.golden_chests = random.sample(range(1, TOTAL_CHESTS + 1), GOLDEN_CHESTS)
    st.session_state.selected_chests = []

# Initialize session state
if "golden_chests" not in st.session_state:
    reset_game()

def calculate_probability(selected_chests):
    """Calculate the probability-based score based on selected chests."""
    gold_found = sum(1 for chest in selected_chests if chest in st.session_state.golden_chests)
    
    # Assign points based on gold found
    points = {0: 0, 1: 10, 2: 25, 3: 50}  # Example scoring system
    return gold_found, points[gold_found]

# Streamlit UI
st.title("Treasure Hunt Probability Challenge 🏴‍☠️")
st.write("Select 3 chests out of 10 and try to find gold!")

# Player Selection
selected_chests = st.multiselect("Choose 3 chests:", list(range(1, TOTAL_CHESTS + 1)), default=st.session_state.selected_chests, max_selections=3)

if len(selected_chests) == 3:
    gold_found, score = calculate_probability(selected_chests)
    st.write(f"You found {gold_found} gold coins!")
    st.write(f"Your score: {score} points")

    # Show the actual gold locations
    st.write("💰 Gold was hidden in chests:", st.session_state.golden_chests)

    # Expected Value Calculation
    probabilities = {
        0: 36 / 120,
        1: 54 / 120,
        2: 27 / 120,
        3: 3 / 120
    }
    ev = sum(probabilities[i] * {0: 0, 1: 10, 2: 25, 3: 50}[i] for i in range(4))
    st.write(f"📊 Expected Value (EV) of the game: {ev:.2f} points")

    if st.button("Restart Game"):
        reset_game()
        st.rerun()
else:
    st.warning("Please select exactly 3 chests to play.")
