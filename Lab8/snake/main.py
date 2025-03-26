import pygame
import random

pygame.init()

# Window dimensions
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Enhanced Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_GREEN = (0, 100, 0)
YELLOW = (255, 255, 0)

# Game variables
score = 0
fruit_eaten = False
level = 1
fruits_per_level = 3
fruits_eaten_total = 0
base_delay = 200
current_delay = base_delay
speed_level = 1

# Snake and fruit initialization
fr_x = random.randrange(1, width//10)*10
fr_y = random.randrange(1, height//10)*10
fruit_coor = [fr_x, fr_y]
head_square = [100, 100]
squares = [[x, 100] for x in range(30, 101, 10)]

# Movement variables
direction = "right"
next_dir = "right"

done = False

def draw_grid():
    """Draw a subtle grid background"""
    for x in range(0, width, 10):
        pygame.draw.line(screen, GRAY, (x, 0), (x, height), 1)
    for y in range(0, height, 10):
        pygame.draw.line(screen, GRAY, (0, y), (width, y), 1)

def game_over(font, size, color):
    """Display game over screen with enhanced visuals"""
    global done
    # Darken background
    overlay = pygame.Surface((width, height))
    overlay.fill((0, 0, 0))
    overlay.set_alpha(200)
    screen.blit(overlay, (0, 0))
    
    g_o_font = pygame.font.SysFont(font, size, bold=True)
    g_o_surface = g_o_font.render(f"Game Over! Score: {score} - Level: {level} - Speed: {speed_level}", True, color)
    g_o_rect = g_o_surface.get_rect(center=(width//2, height//2))
    
    # Add shadow effect
    shadow_surface = g_o_font.render(f"Game Over! Score: {score} - Level: {level} - Speed: {speed_level}", True, BLACK)
    shadow_rect = shadow_surface.get_rect(center=(width//2+2, height//2+2))
    screen.blit(shadow_surface, shadow_rect)
    screen.blit(g_o_surface, g_o_rect)
    
    pygame.display.update()
    pygame.time.delay(4000)
    pygame.quit()

def spawn_fruit():
    """Generate new fruit position not overlapping with snake"""
    while True:
        x = random.randrange(1, width//10)*10
        y = random.randrange(1, height//10)*10
        if [x, y] not in squares:
            return [x, y]

# Main game loop
while not done:
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

    # Collision checks
    for square in squares[:-1]:
        if head_square[0] == square[0] and head_square[1] == square[1]:
            game_over("arial", 45, YELLOW)

    # Movement logic
    if next_dir == "right" and direction != "left":
        direction = "right"
    if next_dir == "up" and direction != "down":
        direction = "up"
    if next_dir == "left" and direction != "right":
        direction = "left"
    if next_dir == "down" and direction != "up":
        direction = "down"

    if direction == "right":
        head_square[0] += 10
    if direction == "left":
        head_square[0] -= 10
    if direction == "up":
        head_square[1] -= 10
    if direction == "down":
        head_square[1] += 10

    if (head_square[0] < 0 or head_square[0] >= width or 
        head_square[1] < 0 or head_square[1] >= height):
        game_over("arial", 45, YELLOW)

    new_square = [head_square[0], head_square[1]]
    squares.append(new_square)
    if not fruit_eaten:
        squares.pop(0)

    if head_square[0] == fruit_coor[0] and head_square[1] == fruit_coor[1]:
        fruit_eaten = True
        score += 10
        fruits_eaten_total += 1
        if fruits_eaten_total % fruits_per_level == 0:
            level += 1
            speed_level += 1
            current_delay = max(50, base_delay - (speed_level-1) * 40)
        fruit_coor = spawn_fruit()
        fruit_eaten = False

    # Drawing section
    screen.fill(BLACK)
    draw_grid()  # Draw background grid

    # Draw stats with shadow
    stats_font = pygame.font.SysFont("arial", 20, bold=True)
    stats_text = f"Score: {score}  Level: {level}  Speed: {speed_level}"
    stats_surface = stats_font.render(stats_text, True, WHITE)
    shadow_surface = stats_font.render(stats_text, True, BLACK)
    screen.blit(shadow_surface, (12, 12))
    screen.blit(stats_surface, (10, 10))

    # Draw fruit with glow effect
    pygame.draw.circle(screen, YELLOW, (fruit_coor[0]+5, fruit_coor[1]+5), 7)  # Glow
    pygame.draw.circle(screen, RED, (fruit_coor[0]+5, fruit_coor[1]+5), 5)     # Fruit

    # Draw snake with gradient effect
    for i, el in enumerate(squares):
        # Gradient from dark green to green based on position
        green_value = min(255, 100 + i * 10)
        color = (0, green_value, 0)
        pygame.draw.rect(screen, color, pygame.Rect(el[0], el[1], 10, 10))
        # Add outline
        pygame.draw.rect(screen, DARK_GREEN, pygame.Rect(el[0], el[1], 10, 10), 1)
    
    # Draw head with distinct color
    pygame.draw.rect(screen, GREEN, pygame.Rect(head_square[0], head_square[1], 10, 10))
    pygame.draw.rect(screen, DARK_GREEN, pygame.Rect(head_square[0], head_square[1], 10, 10), 1)

    pygame.display.flip()
    pygame.time.delay(current_delay)

pygame.quit()