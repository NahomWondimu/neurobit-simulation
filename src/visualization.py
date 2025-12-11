"""Neural pulse visualization in a generated maze.

This module creates an interactive maze where clicking spawns neural pulses
that propagate through the maze based on their neurobit patterns.
"""

import pygame
import random
import time
from src.neurobit_walker import Neurobit, NeuroPulse

# Grid Settings
BOX_WIDTH = 20
BORDER_SIZE = 2
COLS = 10
ROWS = 6

SCREEN_WIDTH = COLS * (BOX_WIDTH + BORDER_SIZE)
SCREEN_HEIGHT = ROWS * (BOX_WIDTH + BORDER_SIZE)

# Colors
BARRIER_COLOR = (230, 58, 58)
PATH_COLOR = (59, 68, 75)
EXIT_FILL_COLOR = (0, 180, 255)
FADE_SPEED = 1.5
GOLD_COLOR = (239, 191, 4)

# --- Setup ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 18)

# --- Maze Graph ---
graph = {}
visited = set()
fade_state = [[0.0 for _ in range(COLS)] for _ in range(ROWS)]
exit_state = [[False for _ in range(COLS)] for _ in range(ROWS)]
pulses = []

# --- Neurobit Factory ---
def spawn_neurobit():
    return Neurobit(
        id=random.randint(1, 9999),
        pattern=random.randint(0, 255),
        mask=random.choice([0xF0, 0xF8, 0x00]),
        action_code=0
    )

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
    edge_cells = [(r, 0) for r in range(ROWS)] + [(r, COLS - 1) for r in range(ROWS)] + \
                 [(0, c) for c in range(1, COLS - 1)] + [(ROWS - 1, c) for c in range(1, COLS - 1)]
    for r, c in random.sample(edge_cells, 5):
        graph.setdefault((r, c), []).append((-1, -1))
        exit_state[r][c] = True

def draw_maze():
    screen.fill(BARRIER_COLOR)
    for (r, c), neighbors in graph.items():
        x = c * (BOX_WIDTH + BORDER_SIZE)
        y = r * (BOX_WIDTH + BORDER_SIZE)
        for nr, nc in neighbors:
            if (nr, nc) != (-1, -1):
                nx, ny = nc * (BOX_WIDTH + BORDER_SIZE), nr * (BOX_WIDTH + BORDER_SIZE)
                pygame.draw.line(screen, PATH_COLOR, (x + BOX_WIDTH // 2, y + BOX_WIDTH // 2),
                                 (nx + BOX_WIDTH // 2, ny + BOX_WIDTH // 2), BOX_WIDTH)
        color_box(r, c, EXIT_FILL_COLOR if exit_state[r][c] else PATH_COLOR)

def draw_fades(dt):
    brightest = max(pulses, key=lambda p: p.ttl, default=None)
    bright_pos = brightest.pos if brightest else None

    for r in range(ROWS):
        for c in range(COLS):
            if fade_state[r][c] > 0:
                fade_state[r][c] -= FADE_SPEED * dt
                fade_state[r][c] = max(fade_state[r][c], 0)
                intensity = int(255 * (fade_state[r][c] / 3.0))

                # Keep gold pulse from being overwritten
                if (r, c) == bright_pos:
                    color_box(r, c, (239, 191, 4))  # Gold
                else:
                    color_box(r, c, (intensity, intensity, intensity))


def write_debug_info(pulses):
    # Doesn't write
    with open('debug.log', 'w') as f:
        for pulse in pulses:
            f.write(f"ID:{pulse.nb.id} PAT:{pulse.nb.pattern:08b} MASK:{pulse.nb.mask:08b} TTL:{pulse.ttl} POS:{pulse.pos}\\n")

def color_box(r, c, color):
    x = c * (BOX_WIDTH + BORDER_SIZE)
    y = r * (BOX_WIDTH + BORDER_SIZE)
    pygame.draw.rect(screen, color, (x + 3, y + 3, BOX_WIDTH - 6, BOX_WIDTH - 6))

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            c, r = mouseX // (BOX_WIDTH + BORDER_SIZE), mouseY // (BOX_WIDTH + BORDER_SIZE)
            if 0 <= r < ROWS and 0 <= c < COLS:
                fade_state[r][c] = 3.0
                nb = spawn_neurobit()
                pulse = NeuroPulse(pos=(r, c), graph=graph, neurobit=nb, ttl=7, exploration_rate=0.1)
                pulses.append(pulse)
    return True

def main():
    generate_maze()
    running = True
    dt = 0

    while running:
        running = handle_events()
        draw_maze()
        draw_fades(dt)

        active_positions = set(pulse.pos for pulse in pulses if pulse.ttl > 0)

        for pulse in pulses[:]:
            new_pulses = pulse.step(blocked_positions=active_positions)
            r, c = pulse.pos
            fade_state[r][c] = 3.0
            if new_pulses:
                pulses.extend(new_pulses)
            if pulse.ttl <= 0:
                pulses.remove(pulse)

        # write_debug_info(pulses)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        time.sleep(0.1)

    pygame.quit()

if __name__ == "__main__":
    main()