import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
TOWER_COLOR = (0, 0, 0)
DISK_COLOR = (0, 0, 255)
BUTTON_COLOR = (0, 255, 0)
BUTTON_TEXT_COLOR = (0, 0, 0)
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 40
BUTTON_MARGIN = 20
FONT_SIZE = 36

# Define Tower of Hanoi parameters
num_disks = 4
towers = [[], [], []]
tower_width = 10
tower_height = 400
tower_spacing = 300
disk_width = [100, 80, 60]
disk_height = 20
disk_spacing = 20
total_steps = 0
current_step = 0

# Initialize towers
for i in range(num_disks, 0, -1):
    towers[0].append(i)

# Create Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower of Hanoi")

# Initialize input field
input_rect = pygame.Rect(20, 20, 200, 40)
input_font = pygame.font.Font(None, FONT_SIZE)
input_text = ""
input_active = False

# Function to draw the towers and disks
def draw():
    screen.fill(BACKGROUND_COLOR)

    for i in range(3):
        pygame.draw.rect(screen, TOWER_COLOR, (i * tower_spacing, HEIGHT - tower_height, tower_width, tower_height))
        for j, disk in enumerate(towers[i]):
            disk_width_actual = disk_width[disk - 1]
            pygame.draw.rect(screen, DISK_COLOR, (i * tower_spacing + (tower_width - disk_width_actual) / 2, HEIGHT - tower_height + j * (disk_height + disk_spacing), disk_width_actual, disk_height))

# Function to draw the "Run" button
def draw_run_button():
    pygame.draw.rect(screen, BUTTON_COLOR, (WIDTH - BUTTON_WIDTH - BUTTON_MARGIN, BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT))
    font = pygame.font.Font(None, FONT_SIZE)
    text = font.render("Run", True, BUTTON_TEXT_COLOR)
    text_rect = text.get_rect(center=(WIDTH - BUTTON_WIDTH / 2 - BUTTON_MARGIN, BUTTON_MARGIN + BUTTON_HEIGHT / 2))
    screen.blit(text, text_rect)

# Function to draw the "Repeat" button
def draw_repeat_button():
    pygame.draw.rect(screen, BUTTON_COLOR, (WIDTH - BUTTON_WIDTH - BUTTON_MARGIN, BUTTON_MARGIN + BUTTON_HEIGHT + BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT))
    font = pygame.font.Font(None, FONT_SIZE)
    text = font.render("Repeat", True, BUTTON_TEXT_COLOR)
    text_rect = text.get_rect(center=(WIDTH - BUTTON_WIDTH / 2 - BUTTON_MARGIN, BUTTON_MARGIN + BUTTON_HEIGHT + BUTTON_MARGIN + BUTTON_HEIGHT / 2))
    screen.blit(text, text_rect)

# Function to draw the step counters
def draw_steps():
    font = pygame.font.Font(None, FONT_SIZE)
    total_steps_text = font.render(f"Total Steps: {total_steps}", True, (0, 0, 0))
    current_step_text = font.render(f"Current Step: {current_step}", True, (0, 0, 0))
    screen.blit(total_steps_text, (20, HEIGHT - 2 * FONT_SIZE))
    screen.blit(current_step_text, (20, HEIGHT - FONT_SIZE))

# Recursive function to solve Tower of Hanoi
def hanoi(n, source, target, auxiliary):
    global current_step
    if n == 1:
        current_step += 1
        move_disk(source, target)
        draw()
        draw_steps()
        pygame.display.flip()
        pygame.time.delay(500)  # Delay for visualization
    else:
        hanoi(n - 1, source, auxiliary, target)
        current_step += 1
        move_disk(source, target)
        draw()
        draw_steps()
        pygame.display.flip()
        pygame.time.delay(500)  # Delay for visualization
        hanoi(n - 1, auxiliary, target, source)

# Function to move a disk from one tower to another
def move_disk(source, target):
    disk = towers[source].pop()
    towers[target].append(disk)

# Game loop
running = True
source_tower = None
target_tower = None
button_run_rect = pygame.Rect(WIDTH - BUTTON_WIDTH - BUTTON_MARGIN, BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT)
button_repeat_rect = pygame.Rect(WIDTH - BUTTON_WIDTH - BUTTON_MARGIN, BUTTON_MARGIN + BUTTON_HEIGHT + BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_run_rect.collidepoint(event.pos) and source_tower is None:
                total_steps = (2 ** num_disks) - 1  # Calculate the total number of steps
                current_step = 0
                hanoi(num_disks, 0, 2, 1)  # Start the Tower of Hanoi algorithm
            elif button_repeat_rect.collidepoint(event.pos):
                # Reset the towers and animation
                towers[0] = list(range(num_disks, 0, -1))
                towers[1] = []
                towers[2] = []
                source_tower = None
                target_tower = None
                current_step = 0
                draw()
        elif event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_RETURN:
                    try:
                        num_disks = int(input_text)
                        towers[0] = list(range(num_disks, 0, -1))
                        towers[1] = []
                        towers[2] = []
                        input_text = ""
                        input_active = False
                        draw()
                    except ValueError:
                        input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    draw()
    draw_run_button()
    draw_repeat_button()
    draw_steps()
    
    # Draw input field
    
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
