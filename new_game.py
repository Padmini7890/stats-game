import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np
import time

# Streamlit UI setup
st.title("Ultimate Statistical Car Racing Game")
st.write("Choose your car wisely, race, and analyze statistics to optimize your performance!")

# Car selection with attributes that vary for different players
car_quality = random.uniform(0.8, 1.2)  # Adds variability to each car
car_types = {
    "Sports Car": (8 * car_quality, 18 * car_quality, 0.3, 0.4, "red"),
    "Truck": (4 * car_quality, 10 * car_quality, 0.15, 0.25, "blue"),
    "Electric Car": (6 * car_quality, 14 * car_quality, 0.2, 0.3, "green")
}
car_choice = st.selectbox("Select your car type:", list(car_types.keys()))
speed, max_speed, acceleration, deceleration, car_color = car_types[car_choice]

# Game variables
fuel = 100  # Fuel percentage
lap_times = []
laps = 0
score = 0

def random_event():
    events = ["tire_puncture", "engine_failure", "fuel_leak", "speed_boost", "crash", "mechanical_issue", "clear"]
    probabilities = [0.1, 0.07, 0.12, 0.08, 0.12, 0.06, 0.45]  # More risk factors
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
fuel -= 0.1 + (speed / max_speed) * 0.2
if fuel <= 0:
    st.write(f"Out of fuel! Game Over. Final Score: {score}")
    st.stop()

# Random Event Handling
if random.random() < 0.07:  # 7% chance every frame
    event = random_event()
    if event != "clear":
        st.write(f"Random event occurred: {event}")
    if event == "tire_puncture":
        speed = max(2, speed - 5)
    elif event == "engine_failure":
        speed = 2
    elif event == "fuel_leak":
        fuel -= 25
    elif event == "speed_boost":
        speed = min(max_speed, speed + 5)
    elif event == "crash":
        st.write("You crashed! Game Over.")
        st.stop()
    elif event == "mechanical_issue":
        speed = max(2, speed - 3)

# Updating Laps and Score
laps += 1
score += 15
lap_time = time.time() - st.session_state.start_time
lap_times.append(lap_time)
st.session_state.start_time = time.time()

# Display Stats
st.write(f"Car Type: {car_choice}")
st.write(f"Car Quality Factor: {car_quality:.2f}")
st.write(f"Current Speed: {speed:.2f}")
st.write(f"Fuel Level: {fuel:.2f}%")
st.write(f"Laps Completed: {laps}")
st.write(f"Score: {score}")

# Visualizing Car Progress
fig, ax = plt.subplots()
ax.barh(["Fuel", "Speed", "Laps"], [fuel, speed, laps], color=["orange", car_color, "gray"])
ax.set_xlim(0, max(100, max_speed))
ax.set_xlabel("Value")
ax.set_title("Car Performance Stats")
st.pyplot(fig)

# Plot Lap Time Analysis
fig, ax = plt.subplots()
ax.plot(lap_times, marker='o', linestyle='-', color=car_color)
ax.set_xlabel("Lap Number")
ax.set_ylabel("Lap Time (s)")
ax.set_title("Lap Time Analysis")
st.pyplot(fig)
