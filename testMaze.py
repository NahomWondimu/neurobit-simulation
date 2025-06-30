"""Interactive maze generation and display using Pygame.

This module creates a maze using depth-first search algorithm and allows
interactive clicking to highlight cells with fading effect.
"""

import pygame
import random

# Grid Settings
BOX_WIDTH = 20
BORDER_SIZE = 2
COLS = 60
ROWS = 30

SCREEN_WIDTH = COLS * (BOX_WIDTH + BORDER_SIZE)
SCREEN_HEIGHT = ROWS * (BOX_WIDTH + BORDER_SIZE)

# Colors
BARRIER_COLOR = (230, 58, 58)    # Red background (walls)
PATH_COLOR = (59, 68, 75)        # Grey (regular path)
EXIT_FILL_COLOR = (0, 180, 255)  # Full cell fill for exits
FADE_SPEED = 0.5                 # How fast clicked boxes fade

# --- Setup ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# --- Maze Graph ---
graph = {}  # (row, col): [(neighbor1), (neighbor2), ...]
visited = set()
fade_state = [[0.0 for _ in range(COLS)] for _ in range(ROWS)]  # <-- updated from click_state
exit_state = [[False for _ in range(COLS)] for _ in range(ROWS)]  # tracks exit locations

def generate_maze():
    def dfs(r, c):
        visited.add((r, c))
        graph[(r, c)] = []

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        random.shuffle(directions)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                dfs(nr, nc)
                graph[(r, c)].append((nr, nc))
                if (nr, nc) not in graph:
                    graph[(nr, nc)] = []
                graph[(nr, nc)].append((r, c))

    dfs(0, 0)
    add_exits()

def add_exits():
    edge_cells = []
    for r in range(ROWS):
        edge_cells.append((r, 0))
        edge_cells.append((r, COLS - 1))
    for c in range(1, COLS - 1):
        edge_cells.append((0, c))
        edge_cells.append((ROWS - 1, c))

    exit_cells = random.sample(edge_cells, 5)
    for cell in exit_cells:
        r, c = cell
        if cell in graph:
            graph[cell].append((-1, -1))
        else:
            graph[cell] = [(-1, -1)]
        exit_state[r][c] = True

def draw_maze():
    screen.fill(BARRIER_COLOR)
    for (r, c), neighbors in graph.items():
        x = c * (BOX_WIDTH + BORDER_SIZE)
        y = r * (BOX_WIDTH + BORDER_SIZE)

        for nr, nc in neighbors:
            if (nr, nc) == (-1, -1):
                pygame.draw.circle(screen, (255, 255, 0), (x + BOX_WIDTH // 2, y + BOX_WIDTH // 2), BOX_WIDTH // 3)
            else:
                nx = nc * (BOX_WIDTH + BORDER_SIZE)
                ny = nr * (BOX_WIDTH + BORDER_SIZE)
                pygame.draw.line(
                    screen,
                    PATH_COLOR,
                    (x + BOX_WIDTH // 2, y + BOX_WIDTH // 2),
                    (nx + BOX_WIDTH // 2, ny + BOX_WIDTH // 2),
                    BOX_WIDTH
                )

        # Use different color if this cell is an exit
        cell_color = EXIT_FILL_COLOR if exit_state[r][c] else PATH_COLOR
        color_box(r, c, cell_color)

def draw_clicks(dt):
    """Draw fading boxes based on their timer."""
    for r in range(ROWS):
        for c in range(COLS):
            if fade_state[r][c] > 0:
                fade_state[r][c] -= FADE_SPEED * dt
                fade_state[r][c] = max(fade_state[r][c], 0)
                intensity = int(255 * (fade_state[r][c] / 3.0))
                color = (intensity, intensity, intensity)
                color_box(r, c, color)

def color_box(row, column, colorChoice):
    x = column * (BOX_WIDTH + BORDER_SIZE)
    y = row * (BOX_WIDTH + BORDER_SIZE)
    pygame.draw.rect(
        screen,
        colorChoice,
        (x + 3, y + 3, BOX_WIDTH - 6, BOX_WIDTH - 6)
    )

def handle_events():
    """Handle clicks to light up a cell."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            c = mouseX // (BOX_WIDTH + BORDER_SIZE)
            r = mouseY // (BOX_WIDTH + BORDER_SIZE)
            if 0 <= r < ROWS and 0 <= c < COLS:
                fade_state[r][c] = 3.0  # full brightness
    return True

def main():
    generate_maze()
    running = True
    dt = 0

    while running:
        running = handle_events()
        draw_maze()
        draw_clicks(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Delta time in seconds

    pygame.quit()

if __name__ == "__main__":
    main()
