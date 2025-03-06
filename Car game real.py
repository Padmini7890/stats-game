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
GRAY = (169, 169, 169)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Car settings
CAR_WIDTH, CAR_HEIGHT = 50, 100
car_x, car_y = WIDTH//2, HEIGHT - 150

# Obstacle settings
obstacle_width, obstacle_height = 50, 100
num_obstacles = 3
obstacles = [{
    'x': random.randint(200, WIDTH - 250),
    'y': random.randint(-600, -100)
} for _ in range(num_obstacles)]
obstacle_speed = 5

# Fuel pickup settings
fuel_pickup = {'x': random.randint(220, WIDTH - 250), 'y': random.randint(-500, -100)}

# Game variables
speed = 5
max_speed = 12
acceleration = 0.1
deceleration = 0.2
fuel = 100  # Fuel percentage
lap_times = []
start_time = pygame.time.get_ticks()
laps = 0
score = 0

# Random events probabilities
def random_event():
    events = ["tire_puncture", "engine_failure", "fuel_leak", "speed_boost", "clear"]
    probabilities = [0.05, 0.03, 0.07, 0.05, 0.8]  # Probabilities sum to 1
    return np.random.choice(events, p=probabilities)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(GRAY)
    
    # Draw road and lanes
    pygame.draw.rect(screen, BLACK, (200, 0, 400, HEIGHT))  # Road
    for i in range(0, HEIGHT, 40):
        pygame.draw.rect(screen, YELLOW, (395, i, 10, 20))  # Lane markings
    
    # Draw car
    pygame.draw.rect(screen, BLUE, (car_x, car_y, CAR_WIDTH, CAR_HEIGHT))
    
    # Draw obstacles
    for obs in obstacles:
        pygame.draw.rect(screen, RED, (obs['x'], obs['y'], obstacle_width, obstacle_height))
        obs['y'] += obstacle_speed
        
        # Reset obstacle if it goes off screen
        if obs['y'] > HEIGHT:
            obs['y'] = random.randint(-600, -100)
            obs['x'] = random.randint(220, WIDTH - 250)
            laps += 1  # Increase lap count
            score += 10  # Increase score
            print(f"Lap {laps} completed! Score: {score}")
    
    # Draw fuel pickup
    pygame.draw.rect(screen, GREEN, (fuel_pickup['x'], fuel_pickup['y'], 40, 40))
    fuel_pickup['y'] += obstacle_speed
    if fuel_pickup['y'] > HEIGHT:
        fuel_pickup['y'] = random.randint(-500, -100)
        fuel_pickup['x'] = random.randint(220, WIDTH - 250)
    
    # Collision detection
    for obs in obstacles:
        if (car_y < obs['y'] + obstacle_height and car_y + CAR_HEIGHT > obs['y'] and
            car_x < obs['x'] + obstacle_width and car_x + CAR_WIDTH > obs['x']):
            print(f"Crash! Game Over. Final Score: {score}")
            running = False
    
    # Fuel pickup collision
    if (car_y < fuel_pickup['y'] + 40 and car_y + CAR_HEIGHT > fuel_pickup['y'] and
        car_x < fuel_pickup['x'] + 40 and car_x + CAR_WIDTH > fuel_pickup['x']):
        fuel = min(100, fuel + 20)
        fuel_pickup['y'] = random.randint(-500, -100)
        fuel_pickup['x'] = random.randint(220, WIDTH - 250)
        print("Picked up fuel! +20")
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 210:
        car_x -= speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - 260:
        car_x += speed
    if keys[pygame.K_UP]:
        speed = min(max_speed, speed + acceleration)  # Accelerate
    if keys[pygame.K_DOWN]:
        speed = max(2, speed - deceleration)  # Decelerate
    
    # Fuel consumption
    fuel -= 0.05 + (speed / max_speed) * 0.1  # Higher speed consumes more fuel
    if fuel <= 0:
        print(f"Out of fuel! Game Over. Final Score: {score}")
        running = False
    
    # Random event occurrence
    if random.random() < 0.01:  # 1% chance every frame
        event = random_event()
        if event != "clear":  # Only print if an actual event occurs
            print(f"Random event occurred: {event}")
        if event == "tire_puncture":
            speed = max(2, speed - 3)
        elif event == "engine_failure":
            speed = 2
        elif event == "fuel_leak":
            fuel -= 15
        elif event == "speed_boost":
            speed = min(max_speed, speed + 3)
    
    pygame.display.update()
    clock.tick(30)

# Lap time analysis
lap_times.append((pygame.time.get_ticks() - start_time) / 1000)
print("Lap Times:", lap_times)

# Visualization
plt.plot(lap_times, marker='o', linestyle='-')
plt.xlabel("Lap Number")
plt.ylabel("Lap Time (s)")
plt.title("Lap Time Analysis")
plt.show()

pygame.quit()
