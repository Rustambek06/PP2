import pygame
import random

# Shape constants
SQUARE = 'SQUARE'
CIRCLE = 'CIRCLE'
TRIANGLE = 'TRIANGLE'
RHOMBUS = 'RHOMBUS'
RIGHT_TRIANGLE = 'RIGHT_TRIANGLE'  # New right triangle constant
EQUILATERAL_TRIANGLE = 'EQUILATERAL_TRIANGLE'  # New equilateral triangle constant

# Window dimensions
dis_width = 640
dis_height = 480
main_screen_size = (dis_width, dis_height)
elements_to_draw = [] 

# Icon bar coordinates
icon_top_bar_height = 50
icon_top_bar_width = 50
icon_rectangle_start_x = 0
icon_rectangle_end_x = 50
icon_circle_start_x = 50
icon_circle_end_x = 100
icon_triangle_start_x = 100
icon_triangle_end_x = 150
icon_rhombus_start_x = 150
icon_rhombus_end_x = 200
icon_eraser_start_x = 200
icon_eraser_end_x = 250
icon_right_tri_start_x = 250  # New right triangle icon position
icon_right_tri_end_x = 300
icon_equil_tri_start_x = 300  # New equilateral triangle icon position
icon_equil_tri_end_x = 350

# Color selector coordinates
icon_red_color_start_y = 50
icon_red_color_end_y = 75
icon_blue_color_start_y = 100
icon_blue_color_end_y = 125
icon_black_color_start_y = 150
icon_black_color_end_y = 175
icon_green_color_start_y = 200
icon_green_color_end_y = 225
icon_yellow_color_start_y = 250
icon_yellow_color_end_y = 275
icon_purple_color_start_y = 300
icon_purple_color_end_y = 325
icon_pink_color_start_y = 350
icon_pink_color_end_y = 375
icon_gray_color_start_y = 400
icon_gray_color_end_y = 425

icon_color_shape_width = 40
icon_color_shape_height = 30

# Color definitions
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (128, 0, 128)
pink = (255, 105, 180)
gray = (128, 128, 128)
top_tab_color = (100, 100, 100)
right_tab_color = (80, 80, 80)

# Function to draw all shapes in the elements list
def draw_all_shapes(screen):
    for element in elements_to_draw:
        if element['shape'] == SQUARE:
            pygame.draw.rect(screen, element['color'], [element['x'], element['y'], 50, 50])
        elif element['shape'] == CIRCLE:
            pygame.draw.circle(screen, element['color'], (element['x'], element['y']), element['radius'])
        elif element['shape'] == TRIANGLE:
            draw_triangle(screen, element['x'], element['y'], element['color'])
        elif element['shape'] == RHOMBUS:
            draw_rhombus(screen, element['x'], element['y'], element['color'])
        elif element['shape'] == RIGHT_TRIANGLE:  # New right triangle drawing
            draw_right_triangle(screen, element['x'], element['y'], element['color'])
        elif element['shape'] == EQUILATERAL_TRIANGLE:  # New equilateral triangle drawing
            draw_equilateral_triangle(screen, element['x'], element['y'], element['color'])

# Draw regular triangle (isosceles)
def draw_triangle(screen, x, y, color):
    points = [(x, y - 25), (x + 25, y + 25), (x - 25, y + 25)]
    pygame.draw.polygon(screen, color, points)

# Draw rhombus shape
def draw_rhombus(screen, x, y, color):
    points = [(x, y - 25), (x + 25, y), (x, y + 25), (x - 25, y)]
    pygame.draw.polygon(screen, color, points)

# New function to draw right triangle
def draw_right_triangle(screen, x, y, color):
    points = [(x, y), (x + 50, y), (x, y + 50)]
    pygame.draw.polygon(screen, color, points)

# New function to draw equilateral triangle
def draw_equilateral_triangle(screen, x, y, color):
    height = 50 * (3 ** 0.5) / 2  # Height of equilateral triangle
    points = [(x, y - height/2), (x + 25, y + height/2), (x - 25, y + height/2)]
    pygame.draw.polygon(screen, color, points)

# Add square to elements list
def add_element_rectangle(x, y, color):
    elements_to_draw.append({'shape': SQUARE, 'x': x, 'y': y, 'color': color})

# Add circle to elements list
def add_element_circle(x, y, color, radius):
    elements_to_draw.append({
        'shape': CIRCLE,
        'x': x,
        'y': y,
        'color': color,
        'radius': radius
    })

# Add regular triangle to elements list
def add_element_triangle(x, y, color):
    elements_to_draw.append({
        'shape': TRIANGLE,
        'x': x,
        'y': y,
        'color': color
    })

# Add rhombus to elements list
def add_element_rhombus(x, y, color):
    elements_to_draw.append({
        'shape': RHOMBUS,
        'x': x,
        'y': y,
        'color': color
    })

# New function to add right triangle to elements list
def add_element_right_triangle(x, y, color):
    elements_to_draw.append({
        'shape': RIGHT_TRIANGLE,
        'x': x,
        'y': y,
        'color': color
    })

# New function to add equilateral triangle to elements list
def add_element_equilateral_triangle(x, y, color):
    elements_to_draw.append({
        'shape': EQUILATERAL_TRIANGLE,
        'x': x,
        'y': y,
        'color': color
    })

# Erase element at clicked position
def erase_element(x, y):
    for i in range(len(elements_to_draw) - 1, -1, -1):
        element = elements_to_draw[i]
        if element['shape'] == SQUARE:
            if (element['x'] <= x <= element['x'] + 50 and 
                element['y'] <= y <= element['y'] + 50):
                elements_to_draw.pop(i)
                return
        elif element['shape'] == CIRCLE:
            dx = x - element['x']
            dy = y - element['y']
            if (dx * dx + dy * dy) <= (element['radius'] * element['radius']):
                elements_to_draw.pop(i)
                return
        elif element['shape'] in [TRIANGLE, RHOMBUS, RIGHT_TRIANGLE, EQUILATERAL_TRIANGLE]:
            if (element['x'] - 25 <= x <= element['x'] + 25 and 
                element['y'] - 25 <= y <= element['y'] + 25):
                elements_to_draw.pop(i)
                return

# Draw the interface icons
def draw_main_icons(screen):
    pygame.draw.rect(screen, top_tab_color, (0, 0, dis_width, 40))
    pygame.draw.rect(screen, right_tab_color, (dis_width - 80, 0, 80, dis_height))
    
    # Existing icons
    pygame.draw.rect(screen, white, (icon_rectangle_start_x + 5, 5, 40, 30))
    pygame.draw.circle(screen, white, (icon_circle_start_x + 25, 20), 15)
    pygame.draw.polygon(screen, white, [(icon_triangle_start_x + 25, 5), 
                                      (icon_triangle_start_x + 45, 35), 
                                      (icon_triangle_start_x + 5, 35)])
    pygame.draw.polygon(screen, white, [(icon_rhombus_start_x + 25, 5), 
                                      (icon_rhombus_start_x + 50, 20), 
                                      (icon_rhombus_start_x + 25, 35), 
                                      (icon_rhombus_start_x, 20)])
    pygame.draw.line(screen, white, (icon_eraser_start_x + 10, 10), 
                    (icon_eraser_end_x - 10, 30), 2)
    pygame.draw.line(screen, white, (icon_eraser_start_x + 10, 30), 
                    (icon_eraser_end_x - 10, 10), 2)
    
    # New icons for right and equilateral triangles
    pygame.draw.polygon(screen, white, [(icon_right_tri_start_x + 5, 5),
                                      (icon_right_tri_start_x + 45, 5),
                                      (icon_right_tri_start_x + 5, 45)])
    pygame.draw.polygon(screen, white, [(icon_equil_tri_start_x + 25, 5),
                                      (icon_equil_tri_start_x + 45, 35),
                                      (icon_equil_tri_start_x + 5, 35)])
    
    # Color selection boxes
    pygame.draw.rect(screen, red, (dis_width - 70, icon_red_color_start_y, icon_color_shape_width, icon_color_shape_height))
    pygame.draw.rect(screen, blue, (dis_width - 70, icon_blue_color_start_y, icon_color_shape_width, icon_color_shape_height))
    pygame.draw.rect(screen, black, (dis_width - 70, icon_black_color_start_y, icon_color_shape_width, icon_color_shape_height))
    pygame.draw.rect(screen, green, (dis_width - 70, icon_green_color_start_y, icon_color_shape_width, icon_color_shape_height))
    pygame.draw.rect(screen, yellow, (dis_width - 70, icon_yellow_color_start_y, icon_color_shape_width, icon_color_shape_height))
    pygame.draw.rect(screen, purple, (dis_width - 70, icon_purple_color_start_y, icon_color_shape_width, icon_color_shape_height))
    pygame.draw.rect(screen, pink, (dis_width - 70, icon_pink_color_start_y, icon_color_shape_width, icon_color_shape_height))
    pygame.draw.rect(screen, gray, (dis_width - 70, icon_gray_color_start_y, icon_color_shape_width, icon_color_shape_height))

def drawLineBetween(screen, index, start, end, width, color_mode):
    # Function to draw gradient lines (unchanged)
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'yellow':
        color = (c2, c2, c1)
    elif color_mode == 'purple':
        color = (c2, c1, c2)
    elif color_mode == 'pink':
        color = (c2, c1, c2)
    elif color_mode == 'gray':
        color = (c2, c2, c2)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def main():
    pygame.init()
    screen = pygame.display.set_mode(main_screen_size)
    clock = pygame.time.Clock()

    # Initialize variables
    is_rectangle_drawer = False
    is_circle_drawer = False
    is_triangle_drawer = False
    is_rhombus_drawer = False
    is_eraser = False
    is_right_tri_drawer = False
    is_equil_tri_drawer = False
    color = black
    drawing = False
    start_pos = (0, 0)
    end_pos = (0, 0)

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = event.pos
                    # Tool selections
                    if position[1] < icon_top_bar_height:
                        if position[0] <= icon_rectangle_end_x and position[0] > 0:
                            is_rectangle_drawer = not is_rectangle_drawer
                            is_circle_drawer = is_triangle_drawer = is_rhombus_drawer = is_eraser = is_right_tri_drawer = is_equil_tri_drawer = False
                        elif position[0] <= icon_circle_end_x and position[0] > icon_circle_start_x:
                            is_circle_drawer = not is_circle_drawer
                            is_rectangle_drawer = is_triangle_drawer = is_rhombus_drawer = is_eraser = is_right_tri_drawer = is_equil_tri_drawer = False
                        elif position[0] <= icon_triangle_end_x and position[0] > icon_triangle_start_x:
                            is_triangle_drawer = not is_triangle_drawer
                            is_rectangle_drawer = is_circle_drawer = is_rhombus_drawer = is_eraser = is_right_tri_drawer = is_equil_tri_drawer = False
                        elif position[0] <= icon_rhombus_end_x and position[0] > icon_rhombus_start_x:
                            is_rhombus_drawer = not is_rhombus_drawer
                            is_rectangle_drawer = is_circle_drawer = is_triangle_drawer = is_eraser = is_right_tri_drawer = is_equil_tri_drawer = False
                        elif position[0] <= icon_eraser_end_x and position[0] > icon_eraser_start_x:
                            is_eraser = not is_eraser
                            is_rectangle_drawer = is_circle_drawer = is_triangle_drawer = is_rhombus_drawer = is_right_tri_drawer = is_equil_tri_drawer = False
                        elif position[0] <= icon_right_tri_end_x and position[0] > icon_right_tri_start_x:
                            is_right_tri_drawer = not is_right_tri_drawer
                            is_rectangle_drawer = is_circle_drawer = is_triangle_drawer = is_rhombus_drawer = is_eraser = is_equil_tri_drawer = False
                        elif position[0] <= icon_equil_tri_end_x and position[0] > icon_equil_tri_start_x:
                            is_equil_tri_drawer = not is_equil_tri_drawer
                            is_rectangle_drawer = is_circle_drawer = is_triangle_drawer = is_rhombus_drawer = is_eraser = is_right_tri_drawer = False
                    # Color selections
                    elif position[0] >= dis_width - 70 and position[0] < dis_width - 70 + icon_color_shape_width:
                        if position[1] > icon_red_color_start_y and position[1] < icon_red_color_end_y:
                            color = red
                        elif position[1] > icon_black_color_start_y and position[1] < icon_black_color_end_y:
                            color = black
                        elif position[1] > icon_blue_color_start_y and position[1] < icon_blue_color_end_y:
                            color = blue
                        elif position[1] > icon_green_color_start_y and position[1] < icon_green_color_end_y:
                            color = green
                        elif position[1] > icon_yellow_color_start_y and position[1] < icon_yellow_color_end_y:
                            color = yellow
                        elif position[1] > icon_purple_color_start_y and position[1] < icon_purple_color_end_y:
                            color = purple
                        elif position[1] > icon_pink_color_start_y and position[1] < icon_pink_color_end_y:
                            color = pink
                        elif position[1] > icon_gray_color_start_y and position[1] < icon_gray_color_end_y:
                            color = gray
                    # Start drawing
                    elif any([is_rectangle_drawer, is_circle_drawer, is_triangle_drawer, 
                             is_rhombus_drawer, is_right_tri_drawer, is_equil_tri_drawer]):
                        drawing = True
                        start_pos = position
                        end_pos = position
                    elif is_eraser:
                        erase_element(position[0], position[1])

            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    end_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    drawing = False
                    # Calculate dimensions
                    width = abs(end_pos[0] - start_pos[0])
                    height = abs(end_pos[1] - start_pos[1])
                    x = min(start_pos[0], end_pos[0])
                    y = min(start_pos[1], end_pos[1])
                    
                    # Draw final shape
                    if is_rectangle_drawer:
                        elements_to_draw.append({'shape': SQUARE, 'x': x, 'y': y, 'color': color, 'width': width, 'height': height})
                    elif is_circle_drawer:
                        radius = max(width, height) // 2
                        center_x = x + width // 2
                        center_y = y + height // 2
                        add_element_circle(center_x, center_y, color, radius)
                    elif is_triangle_drawer:
                        elements_to_draw.append({'shape': TRIANGLE, 'x': x + width//2, 'y': y + height//2, 'color': color, 'width': width, 'height': height})
                    elif is_rhombus_drawer:
                        elements_to_draw.append({'shape': RHOMBUS, 'x': x + width//2, 'y': y + height//2, 'color': color, 'width': width, 'height': height})
                    elif is_right_tri_drawer:
                        elements_to_draw.append({'shape': RIGHT_TRIANGLE, 'x': x, 'y': y, 'color': color, 'width': width, 'height': height})
                    elif is_equil_tri_drawer:
                        elements_to_draw.append({'shape': EQUILATERAL_TRIANGLE, 'x': x + width//2, 'y': y + height//2, 'color': color, 'width': width, 'height': height})

        # Drawing
        screen.fill((255, 255, 255))
        
        # Draw preview rectangle while dragging
        if drawing:
            preview_x = min(start_pos[0], end_pos[0])
            preview_y = min(start_pos[1], end_pos[1])
            preview_width = abs(end_pos[0] - start_pos[0])
            preview_height = abs(end_pos[1] - start_pos[1])
            pygame.draw.rect(screen, gray, (preview_x, preview_y, preview_width, preview_height), 1)

        # Update draw_all_shapes function to handle new size parameters
        for element in elements_to_draw:
            if element['shape'] == SQUARE:
                pygame.draw.rect(screen, element['color'], [element['x'], element['y'], 
                                                          element.get('width', 50), element.get('height', 50)])
            elif element['shape'] == CIRCLE:
                pygame.draw.circle(screen, element['color'], (element['x'], element['y']), element['radius'])
            elif element['shape'] == TRIANGLE:
                width = element.get('width', 50)
                height = element.get('height', 50)
                points = [(element['x'], element['y'] - height/2), 
                         (element['x'] + width/2, element['y'] + height/2), 
                         (element['x'] - width/2, element['y'] + height/2)]
                pygame.draw.polygon(screen, element['color'], points)
            elif element['shape'] == RHOMBUS:
                width = element.get('width', 50)
                height = element.get('height', 50)
                points = [(element['x'], element['y'] - height/2), 
                         (element['x'] + width/2, element['y']), 
                         (element['x'], element['y'] + height/2), 
                         (element['x'] - width/2, element['y'])]
                pygame.draw.polygon(screen, element['color'], points)
            elif element['shape'] == RIGHT_TRIANGLE:
                width = element.get('width', 50)
                height = element.get('height', 50)
                points = [(element['x'], element['y']), 
                         (element['x'] + width, element['y']), 
                         (element['x'], element['y'] + height)]
                pygame.draw.polygon(screen, element['color'], points)
            elif element['shape'] == EQUILATERAL_TRIANGLE:
                width = element.get('width', 50)
                height = element.get('height', 50)
                points = [(element['x'], element['y'] - height/2), 
                         (element['x'] + width/2, element['y'] + height/2), 
                         (element['x'] - width/2, element['y'] + height/2)]
                pygame.draw.polygon(screen, element['color'], points)

        draw_main_icons(screen)
        pygame.display.flip()
        clock.tick(60)

main()