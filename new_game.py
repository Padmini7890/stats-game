import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np
import time

# Streamlit UI setup
st.title("Statistical Car Racing Game")
st.write("Use the controls to simulate the race and track statistics.")

# Game variables
speed = 5
max_speed = 12
acceleration = 0.1
deceleration = 0.2
fuel = 100  # Fuel percentage
lap_times = []
laps = 0
score = 0

def random_event():
    events = ["tire_puncture", "engine_failure", "fuel_leak", "speed_boost", "clear"]
    probabilities = [0.05, 0.03, 0.07, 0.05, 0.8]  # Probabilities sum to 1
    return np.random.choice(events, p=probabilities)

if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

# Streamlit Controls
left, right = st.columns(2)
with left:
    accelerate = st.button("Accelerate")
    decelerate = st.button("Decelerate")
with right:
    move_left = st.button("Move Left")
    move_right = st.button("Move Right")

# Game Logic
if accelerate:
    speed = min(max_speed, speed + acceleration)
if decelerate:
    speed = max(2, speed - deceleration)

# Fuel Consumption
fuel -= 0.05 + (speed / max_speed) * 0.1
if fuel <= 0:
    st.write(f"Out of fuel! Game Over. Final Score: {score}")
    st.stop()

# Random Event Handling
if random.random() < 0.01:  # 1% chance every frame
    event = random_event()
    if event != "clear":
        st.write(f"Random event occurred: {event}")
    if event == "tire_puncture":
        speed = max(2, speed - 3)
    elif event == "engine_failure":
        speed = 2
    elif event == "fuel_leak":
        fuel -= 15
    elif event == "speed_boost":
        speed = min(max_speed, speed + 3)

# Updating Laps and Score
laps += 1
score += 10
lap_time = time.time() - st.session_state.start_time
lap_times.append(lap_time)
st.session_state.start_time = time.time()

# Display Stats
st.write(f"Current Speed: {speed}")
st.write(f"Fuel Level: {fuel}%")
st.write(f"Laps Completed: {laps}")
st.write(f"Score: {score}")

# Plot Lap Time Analysis
fig, ax = plt.subplots()
ax.plot(lap_times, marker='o', linestyle='-')
ax.set_xlabel("Lap Number")
ax.set_ylabel("Lap Time (s)")
ax.set_title("Lap Time Analysis")
st.pyplot(fig)
