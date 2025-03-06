import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np
import time

# Streamlit UI setup
st.title("Ultimate Multiplayer Statistical Car Racing Game")
st.write("Choose your car wisely, race against others, and analyze statistics to optimize your performance!")

# Number of players
num_players = st.slider("Select number of players:", 2, 4, 2)

# Car selection with attributes that vary for different players
car_types = {
    "Sports Car": (8, 18, 0.3, 0.4, "red"),
    "Truck": (4, 10, 0.15, 0.25, "blue"),
    "Electric Car": (6, 14, 0.2, 0.3, "green")
}
players = []
for i in range(num_players):
    st.subheader(f"Player {i+1}")
    car_choice = st.selectbox(f"Select your car type (Player {i+1}):", list(car_types.keys()), key=f"car_{i}")
    car_quality = random.uniform(0.8, 1.2)
    speed, max_speed, acceleration, deceleration, car_color = [x * car_quality if isinstance(x, (int, float)) else x for x in car_types[car_choice]]
    players.append({
        "name": f"Player {i+1}",
        "car": car_choice,
        "speed": speed,
        "max_speed": max_speed,
        "acceleration": acceleration,
        "deceleration": deceleration,
        "color": car_color,
        "fuel": 100,
        "laps": 0,
        "score": 0,
        "lap_times": [],
        "start_time": time.time()
    })

# Random event probability

def random_event():
    events = ["tire_puncture", "engine_failure", "fuel_leak", "speed_boost", "crash", "mechanical_issue", "clear"]
    probabilities = [0.1, 0.07, 0.12, 0.08, 0.12, 0.06, 0.45]  # More risk factors
    return np.random.choice(events, p=probabilities)

# Streamlit Controls
for player in players:
    st.subheader(f"{player['name']} Controls")
    left, right = st.columns(2)
    with left:
        if st.button(f"Accelerate {player['name']}"):
            player["speed"] = min(player["max_speed"], player["speed"] + player["acceleration"])
        if st.button(f"Decelerate {player['name']}"):
            player["speed"] = max(2, player["speed"] - player["deceleration"])
    with right:
        st.button(f"Move Left {player['name']}")
        st.button(f"Move Right {player['name']}")

# Update game logic
for player in players:
    player["fuel"] -= 0.1 + (player["speed"] / player["max_speed"]) * 0.2
    if player["fuel"] <= 0:
        st.write(f"{player['name']} is out of fuel! Final Score: {player['score']}")
        continue
    if random.random() < 0.07:
        event = random_event()
        if event != "clear":
            st.write(f"{player['name']} encountered a {event}")
        if event == "tire_puncture":
            player["speed"] = max(2, player["speed"] - 5)
        elif event == "engine_failure":
            player["speed"] = 2
        elif event == "fuel_leak":
            player["fuel"] -= 25
        elif event == "speed_boost":
            player["speed"] = min(player["max_speed"], player["speed"] + 5)
        elif event == "crash":
            st.write(f"{player['name']} crashed! Game Over.")
            continue
        elif event == "mechanical_issue":
            player["speed"] = max(2, player["speed"] - 3)
    player["laps"] += 1
    player["score"] += 15
    lap_time = time.time() - player["start_time"]
    player["lap_times"].append(lap_time)
    player["start_time"] = time.time()

# Display stats
for player in players:
    st.write(f"**{player['name']} (Car: {player['car']})**")
    st.write(f"Current Speed: {player['speed']:.2f}")
    st.write(f"Fuel Level: {player['fuel']:.2f}%")
    st.write(f"Laps Completed: {player['laps']}")
    st.write(f"Score: {player['score']}")

# Visualizing player performance
fig, ax = plt.subplots()
for player in players:
    ax.plot(player["lap_times"], marker='o', linestyle='-', label=player["name"], color=player["color"])
ax.set_xlabel("Lap Number")
ax.set_ylabel("Lap Time (s)")
ax.set_title("Lap Time Analysis for Players")
ax.legend()
st.pyplot(fig)
