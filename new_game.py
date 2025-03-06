import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np
import time

# Streamlit UI setup
st.title("Advanced Statistical Car Racing Game")
st.write("Choose your car type, race, and analyze the statistics!")

# Car selection
car_types = {"Sports Car": (8, 18, 0.2, 0.3), "Truck": (4, 10, 0.1, 0.2), "Electric Car": (6, 14, 0.15, 0.25)}
car_choice = st.selectbox("Select your car type:", list(car_types.keys()))
speed, max_speed, acceleration, deceleration = car_types[car_choice]

# Game variables
fuel = 100  # Fuel percentage
lap_times = []
laps = 0
score = 0

# Adjust random event probabilities for more challenges
def random_event():
    events = ["tire_puncture", "engine_failure", "fuel_leak", "speed_boost", "crash", "clear"]
    probabilities = [0.08, 0.05, 0.10, 0.07, 0.1, 0.6]  # Higher failure chances
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
fuel -= 0.08 + (speed / max_speed) * 0.15
if fuel <= 0:
    st.write(f"Out of fuel! Game Over. Final Score: {score}")
    st.stop()

# Random Event Handling
if random.random() < 0.05:  # 5% chance every frame
    event = random_event()
    if event != "clear":
        st.write(f"Random event occurred: {event}")
    if event == "tire_puncture":
        speed = max(2, speed - 4)
    elif event == "engine_failure":
        speed = 2
    elif event == "fuel_leak":
        fuel -= 20
    elif event == "speed_boost":
        speed = min(max_speed, speed + 4)
    elif event == "crash":
        st.write("You crashed! Game Over.")
        st.stop()

# Updating Laps and Score
laps += 1
score += 10
lap_time = time.time() - st.session_state.start_time
lap_times.append(lap_time)
st.session_state.start_time = time.time()

# Display Stats
st.write(f"Car Type: {car_choice}")
st.write(f"Current Speed: {speed}")
st.write(f"Fuel Level: {fuel}%")
st.write(f"Laps Completed: {laps}")
st.write(f"Score: {score}")

# Plot Lap Time Analysis
fig, ax = plt.subplots()
ax.plot(lap_times, marker='o', linestyle='-', color='r')
ax.set_xlabel("Lap Number")
ax.set_ylabel("Lap Time (s)")
ax.set_title("Lap Time Analysis")
st.pyplot(fig)
