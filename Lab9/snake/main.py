import pygame
import random
from collections import namedtuple

pygame.init()

# Window dimensions
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Enhanced Snake Game with Timed Food")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_GREEN = (0, 100, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)  # New color for special food
PURPLE = (128, 0, 128)  # New color for rare food

# Food type definition with weights and properties
FoodType = namedtuple('FoodType', ['color', 'weight', 'points', 'duration'])  # duration in milliseconds
FOOD_TYPES = [
    FoodType(RED, 70, 10, 10000),    # Common food: 70% chance, 10 points, 10s
    FoodType(BLUE, 20, 25, 5000),    # Special food: 20% chance, 25 points, 5s
    FoodType(PURPLE, 10, 50, 3000)   # Rare food: 10% chance, 50 points, 3s
]

# Game variables
score = 0
level = 1
fruits_per_level = 3
fruits_eaten_total = 0
base_delay = 200
current_delay = base_delay
speed_level = 1

# Snake initialization
head_square = [100, 100]
squares = [[x, 100] for x in range(30, 101, 10)]
direction = "right"
next_dir = "right"

# Food management
class Food:
    def __init__(self, position, food_type, spawn_time):
        self.position = position
        self.food_type = food_type
        self.spawn_time = spawn_time
    
    def is_expired(self, current_time):
        return current_time - self.spawn_time > self.food_type.duration

current_food = None
done = False

def draw_grid():
    """Draw a subtle grid background"""
    for x in range(0, width, 10):
        pygame.draw.line(screen, GRAY, (x, 0), (x, height), 1)
    for y in range(0, height, 10):
        pygame.draw.line(screen, GRAY, (0, y), (width, y), 1)

def game_over(font, size, color):

    global done
    overlay = pygame.Surface((width, height))
    overlay.fill((0, 0, 0))
    overlay.set_alpha(200)
    screen.blit(overlay, (0, 0))
    
    g_o_font = pygame.font.SysFont(font, size, bold=True)
    g_o_surface = g_o_font.render(f"Game Over! Score: {score} - Level: {level} - Speed: {speed_level}", True, color)
    g_o_rect = g_o_surface.get_rect(center=(width//2, height//2))
    
    shadow_surface = g_o_font.render(f"Game Over! Score: {score} - Level: {level} - Speed: {speed_level}", True, BLACK)
    shadow_rect = shadow_surface.get_rect(center=(width//2+2, height//2+2))
    screen.blit(shadow_surface, shadow_rect)
    screen.blit(g_o_surface, g_o_rect)
    
    pygame.display.update()
    pygame.time.delay(4000)
    pygame.quit()

def spawn_food():
    """Generate new food with weighted random selection"""
    while True:
        x = random.randrange(1, width//10)*10
        y = random.randrange(1, height//10)*10
        if [x, y] not in squares:
            # Weighted random selection of food type
            food_type = random.choices(FOOD_TYPES, weights=[ft.weight for ft in FOOD_TYPES], k=1)[0]
            return Food([x, y], food_type, pygame.time.get_ticks())

# Initial food spawn
current_food = spawn_food()

# Main game loop
clock = pygame.time.Clock()
while not done:
    current_time = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                next_dir = "down"
            if event.key == pygame.K_UP:
                next_dir = "up"
            if event.key == pygame.K_LEFT:
                next_dir = "left"
            if event.key == pygame.K_RIGHT:
                next_dir = "right"

    # Check for snake collision with itself
    for square in squares[:-1]:
        if head_square[0] == square[0] and head_square[1] == square[1]:
            game_over("arial", 45, YELLOW)

    # Update direction based on input
    if next_dir == "right" and direction != "left":
        direction = "right"
    if next_dir == "up" and direction != "down":
        direction = "up"
    if next_dir == "left" and direction != "right":
        direction = "left"
    if next_dir == "down" and direction != "up":
        direction = "down"

    # Move snake
    if direction == "right":
        head_square[0] += 10
    if direction == "left":
        head_square[0] -= 10
    if direction == "up":
        head_square[1] -= 10
    if direction == "down":
        head_square[1] += 10

    # Check wall collision
    if (head_square[0] < 0 or head_square[0] >= width or 
        head_square[1] < 0 or head_square[1] >= height):
        game_over("arial", 45, YELLOW)

    # Update snake body
    new_square = [head_square[0], head_square[1]]
    squares.append(new_square)
    squares.pop(0)  # Remove tail unless food is eaten

    # Check food collision and timer
    fruit_eaten = False
    if head_square[0] == current_food.position[0] and head_square[1] == current_food.position[1]:
        fruit_eaten = True
        score += current_food.food_type.points
        fruits_eaten_total += 1
        if fruits_eaten_total % fruits_per_level == 0:
            level += 1
            speed_level += 1
            current_delay = max(50, base_delay - (speed_level-1) * 40)
        current_food = spawn_food()
    elif current_food.is_expired(current_time):
        current_food = spawn_food()  # Respawn if food expires

    if fruit_eaten:
        # Add new segment to snake when food is eaten
        squares.insert(0, squares[0].copy())

    # Drawing section
    screen.fill(BLACK)
    draw_grid()

    # Draw stats with shadow
    stats_font = pygame.font.SysFont("arial", 20, bold=True)
    stats_text = f"Score: {score}  Level: {level}  Speed: {speed_level}"
    stats_surface = stats_font.render(stats_text, True, WHITE)
    shadow_surface = stats_font.render(stats_text, True, BLACK)
    screen.blit(shadow_surface, (12, 12))
    screen.blit(stats_surface, (10, 10))

    # Draw food with glow effect and timer indication
    food_color = current_food.food_type.color
    time_left = max(0, current_food.food_type.duration - (current_time - current_food.spawn_time))
    alpha = int((time_left / current_food.food_type.duration) * 255)  # Fade effect
    
    glow_surface = pygame.Surface((14, 14), pygame.SRCALPHA)
    pygame.draw.circle(glow_surface, (*YELLOW, 100), (7, 7), 7)
    screen.blit(glow_surface, (current_food.position[0]-2, current_food.position[1]-2))
    
    food_surface = pygame.Surface((10, 10), pygame.SRCALPHA)
    pygame.draw.circle(food_surface, (*food_color, alpha), (5, 5), 5)
    screen.blit(food_surface, (current_food.position[0], current_food.position[1]))

    # Draw snake with gradient effect
    for i, el in enumerate(squares):
        green_value = min(255, 100 + i * 10)
        color = (0, green_value, 0)
        pygame.draw.rect(screen, color, pygame.Rect(el[0], el[1], 10, 10))
        pygame.draw.rect(screen, DARK_GREEN, pygame.Rect(el[0], el[1], 10, 10), 1)
    
    # Draw head
    pygame.draw.rect(screen, GREEN, pygame.Rect(head_square[0], head_square[1], 10, 10))
    pygame.draw.rect(screen, DARK_GREEN, pygame.Rect(head_square[0], head_square[1], 10, 10), 1)

    pygame.display.flip()
    pygame.time.delay(current_delay)
    clock.tick(60)  # Control frame rate

pygame.quit()