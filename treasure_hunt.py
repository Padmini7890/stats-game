import streamlit as st
import random
from itertools import combinations

# Game Setup
TOTAL_CHESTS = 10
GOLDEN_CHESTS = 3  # Number of chests with gold
BLUFF_CHESTS = 2  # Number of fake gold chests

def reset_game():
    st.session_state.selected_chests = []
    st.session_state.golden_chests = random.sample(range(1, TOTAL_CHESTS + 1), GOLDEN_CHESTS)
    remaining_chests = [chest for chest in range(1, TOTAL_CHESTS + 1) if chest not in st.session_state.golden_chests]
    st.session_state.bluff_chests = random.sample(remaining_chests, BLUFF_CHESTS)
    st.session_state.rounds_played = 0
    st.session_state.total_score = 0
    st.session_state.history = []
    st.session_state.gold_history = []
    st.session_state.leaderboard = {}
    st.session_state.player_name = ""

def get_dynamic_hint(golden_chests, bluff_chests):
    """Generate a dynamic hint based on the actual gold locations."""
    min_gold, max_gold = min(golden_chests), max(golden_chests)
    avg_gold = sum(golden_chests) / len(golden_chests)
    hints = [
        f"A pirate whispered that treasures are not too far from chest {random.choice(golden_chests) - random.choice([-1, 1])}...",
        f"Maps show that the wealthiest finds are often between chests {min_gold} and {max_gold}...",
        f"Sailors say gold favors numbers near {round(avg_gold)} more than the rest...",
        "Some say lucky numbers come in groups, others think they avoid the corners...",
        f"Beware! Some chests hold fool's gold—avoid {random.choice(bluff_chests)}..."
    ]
    return random.choice(hints)

def get_past_distribution():
    """Analyze past gold distributions to help players make better choices."""
    all_gold = [chest for round_data in st.session_state.gold_history for chest in round_data]
    if not all_gold:
        return "No past data yet. Make your best guess!"
    chest_counts = {chest: all_gold.count(chest) for chest in range(1, TOTAL_CHESTS + 1)}
    sorted_chests = sorted(chest_counts.items(), key=lambda x: x[1], reverse=True)
    return f"Past data suggests chests {sorted_chests[0][0]} and {sorted_chests[1][0]} have been lucky before!"

# Initialize session state
if "golden_chests" not in st.session_state:
    reset_game()

def calculate_probability(selected_chests):
    """Calculate the probability-based score based on selected chests."""
    gold_found = sum(1 for chest in selected_chests if chest in st.session_state.golden_chests)
    bluff_found = sum(1 for chest in selected_chests if chest in st.session_state.bluff_chests)
    points = {0: 0, 1: 10, 2: 25, 3: 50}  # Scoring system
    score = points[gold_found] - (bluff_found * 5)  # Bluff chests reduce score
    return gold_found, bluff_found, max(0, score)

# Streamlit UI
st.title("Treasure Hunt Probability Challenge 🏴‍☠️")

# Player Name Input
player_name = st.text_input("Enter your name:")
if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = {}
st.write("Select 3 chests out of 10 and try to find gold!")

# Dynamic Hint System
st.write(f"💡 Hint: {get_dynamic_hint(st.session_state.golden_chests, st.session_state.bluff_chests)}")

# Statistical Learning Mode
st.write(f"📊 Insight: {get_past_distribution()}")

# Player Selection
selected_chests = st.multiselect("Choose 3 chests:", list(range(1, TOTAL_CHESTS + 1)), default=[], max_selections=3)

if len(selected_chests) == 3 and player_name:
    if player_name not in st.session_state.leaderboard:
        st.session_state.leaderboard[player_name] = 0
    st.session_state.rounds_played += 1
    gold_found, bluff_found, score = calculate_probability(selected_chests)
    st.write(f"You found {gold_found} gold coins and {bluff_found} fake gold chests!")
    st.write(f"Your score: {score} points")
    st.session_state.leaderboard[player_name] += score
    st.session_state.total_score += score
    st.session_state.history.append(score)
    st.session_state.gold_history.append(st.session_state.golden_chests)

    # Show the actual gold locations
    st.write("💰 Gold was hidden in chests:", st.session_state.golden_chests)
    st.write("⚠️ Bluff chests (fake gold) were in:", st.session_state.bluff_chests)

    # Expected Value Calculation
    probabilities = {
        0: 36 / 120,
        1: 54 / 120,
        2: 27 / 120,
        3: 3 / 120
    }
    ev = sum(probabilities[i] * {0: 0, 1: 10, 2: 25, 3: 50}[i] for i in range(4))
    st.write(f"📊 Expected Value (EV) of the game: {ev:.2f} points")

    st.write("### Game Statistics 📊")
st.write(f"Total Rounds Played: {st.session_state.rounds_played}")
st.write(f"Average Score: {st.session_state.total_score / max(1, st.session_state.rounds_played):.2f}")
st.bar_chart({"Rounds": list(range(1, st.session_state.rounds_played + 1)), "Scores": st.session_state.history})

st.write("### Leaderboard 🏆")
leaderboard_sorted = sorted(st.session_state.leaderboard.items(), key=lambda x: x[1], reverse=True)
for rank, (name, score) in enumerate(leaderboard_sorted[:5], 1):
    st.write(f"{rank}. {name}: {score} points")

if st.button("Restart Game"):
    reset_game()
    st.rerun()
else:
    st.warning("Please select exactly 3 chests to play.")
