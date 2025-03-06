"""
Car Racing Game with Statistical Analysis

This game simulates a simple car racing experience using pygame. It includes:
- Basic car movement
- Fuel consumption tracking
- Random probability-based events affecting gameplay
- Lap time recording and statistical visualization

Author: [Your Name]
GitHub: [Your GitHub Repo]
"""

import pygame
import random
import matplotlib.pyplot as plt
import numpy as np

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Statistical Car Racing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Load car image (ensure 'car.png' is in the working directory)
car = pygame.image.load("car.png")
car = pygame.transform.scale(car, (50, 100))
car_x, car_y = WIDTH//2, HEIGHT - 150

# Game variables
speed = 5
fuel = 100  # Fuel percentage
lap_times = []
start_time = pygame.time.get_ticks()

# Function for probability-based random events
def random_event():
    events = {
        "tire_puncture": 0.05,
        "engine_failure": 0.03,
        "fuel_leak": 0.07,
        "clear": 0.85
    }
    return random.choices(list(events.keys()), weights=events.values())[0]

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    screen.blit(car, (car_x, car_y))
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Car movement controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - 50:
        car_x += speed
    if keys[pygame.K_UP] and car_y > 0:
        car_y -= speed
    if keys[pygame.K_DOWN] and car_y < HEIGHT - 100:
        car_y += speed
    
    # Fuel consumption
    fuel -= 0.05
    if fuel <= 0:
        print("Out of fuel! Game Over.")
        running = False
    
    # Trigger random event occasionally
    if random.random() < 0.01:  # 1% chance per frame
        event = random_event()
        print(f"Random event: {event}")
        if event == "tire_puncture":
            speed -= 2
        elif event == "engine_failure":
            speed = 2
        elif event == "fuel_leak":
            fuel -= 10
    
    pygame.display.update()
    clock.tick(30)

# Record lap time
lap_times.append((pygame.time.get_ticks() - start_time) / 1000)
print("Lap Times:", lap_times)

# Generate Lap Time Analysis Graph
plt.plot(lap_times, marker='o', linestyle='-')
plt.xlabel("Lap Number")
plt.ylabel("Lap Time (s)")
plt.title("Lap Time Analysis")
plt.show()

pygame.quit()
