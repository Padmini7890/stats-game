import streamlit as st
import random
from itertools import combinations

# Level Configuration
LEVELS = {
    "Easy": 10,
    "Medium": 15,
    "Hard": 20
}
GOLDEN_CHESTS = 3  # Fixed for all levels
BLUFF_CHESTS_RATIO = 0.2  # 20% of total chests as bluff chests

def reset_game():
    st.session_state.selected_chests = []
    st.session_state.level = "Easy"
    total_chests = LEVELS[st.session_state.level]
    st.session_state.golden_chests = random.sample(range(1, total_chests + 1), GOLDEN_CHESTS)
    remaining_chests = [chest for chest in range(1, total_chests + 1) if chest not in st.session_state.golden_chests]
    bluff_count = max(1, int(total_chests * BLUFF_CHESTS_RATIO))
    st.session_state.bluff_chests = random.sample(remaining_chests, bluff_count)
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

# Initialize session state
if "golden_chests" not in st.session_state:
    reset_game()

# Streamlit UI
st.title("Treasure Hunt Probability Challenge 🏴‍☠️")

# Player Name Input
player_name = st.text_input("Enter your name:")
if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = {}

# Level Selection
difficulty = st.selectbox("Select Difficulty Level:", list(LEVELS.keys()), index=list(LEVELS.keys()).index(st.session_state.level))
if difficulty != st.session_state.level:
    st.session_state.level = difficulty
    reset_game()

total_chests = LEVELS[st.session_state.level]
st.write(f"Select 3 chests out of {total_chests} and try to find gold!")

# Dynamic Hint System
st.write(f"💡 Hint: {get_dynamic_hint(st.session_state.golden_chests, st.session_state.bluff_chests)}")

# Player Selection
selected_chests = st.multiselect("Choose 3 chests:", list(range(1, total_chests + 1)), default=[], max_selections=3)

if len(selected_chests) == 3 and player_name:
    if player_name not in st.session_state.leaderboard:
        st.session_state.leaderboard[player_name] = 0
    st.session_state.rounds_played += 1
    gold_found = sum(1 for chest in selected_chests if chest in st.session_state.golden_chests)
    bluff_found = sum(1 for chest in selected_chests if chest in st.session_state.bluff_chests)
    points = {0: 0, 1: 10, 2: 25, 3: 50}
    score = points[gold_found] - (bluff_found * 5)
    st.session_state.leaderboard[player_name] += max(0, score)
    st.session_state.total_score += max(0, score)
    st.session_state.history.append(score)
    st.session_state.gold_history.append(st.session_state.golden_chests)

    st.write(f"You found {gold_found} gold coins and {bluff_found} fake gold chests!")
    st.write(f"Your score: {score} points")
    st.write("💰 Gold was hidden in chests:", st.session_state.golden_chests)
    st.write("⚠️ Bluff chests (fake gold) were in:", st.session_state.bluff_chests)

# Leaderboard
st.write("### Leaderboard 🏆")
leaderboard_sorted = sorted(st.session_state.leaderboard.items(), key=lambda x: x[1], reverse=True)
for rank, (name, score) in enumerate(leaderboard_sorted[:5], 1):
    st.write(f"{rank}. {name}: {score} points")

if st.button("Restart Game"):
    reset_game()
    st.rerun()
else:
    st.warning("Please select exactly 3 chests to play.")
