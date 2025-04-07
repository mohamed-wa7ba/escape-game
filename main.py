import pygame
import random
from collections import deque

#This color palette
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# size of network
CELL_SIZE = 40
GRID_WIDTH = 10
GRID_HEIGHT = 10

def create_prison():
    grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    for i in range(GRID_WIDTH):
        grid[0][i] = 1
        grid[GRID_HEIGHT-1][i] = 1
    for i in range(GRID_HEIGHT):
        grid[i][0] = 1
        grid[i][GRID_WIDTH-1] = 1

    # goal and player
    grid[1][1] = 3  # player
    grid[GRID_HEIGHT-2][GRID_WIDTH-2] = 4  # goal

    # Guard placement (random)
    for _ in range(5):
        x, y = random.randint(1, GRID_WIDTH-2), random.randint(1, GRID_HEIGHT-2)
        if grid[y][x] == 0:
            grid[y][x] = 2

    return grid

# BFS path finding algorithm
def bfs(grid, start, end):
    queue = deque([start])
    visited = set([start])
    parent = {}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            return path[::-1]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT:
                if grid[ny][nx] != 1 and grid[ny][nx] != 2 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)
                    queue.append((nx, ny))
    return None

# رسم الشبكة
def draw_grid(screen, grid, path=[]):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if grid[y][x] == 0:  # road
                pygame.draw.rect(screen, WHITE, rect)
            elif grid[y][x] == 1:  # حائط
                pygame.draw.rect(screen, BLACK, rect)
            elif grid[y][x] == 2:  # wall
                pygame.draw.rect(screen, RED, rect)
            elif grid[y][x] == 3:  # player
                pygame.draw.rect(screen, BLUE, rect)
            elif grid[y][x] == 4:  # goal
                pygame.draw.rect(screen, GREEN, rect)

            # draw the path if found.
            if (x, y) in path:
                pygame.draw.circle(screen, (0, 255, 255), (x * CELL_SIZE + CELL_SIZE//2, y * CELL_SIZE + CELL_SIZE//2), 5)

# main game
def main():
    pygame.init()
    screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
    pygame.display.set_caption("Prison Escape - BFS Pathfinding")

    grid = create_prison()
    player_pos = (1, 1)
    end_pos = (GRID_WIDTH-2, GRID_HEIGHT-2)
    path = []
    running = True

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                x, y = player_pos
                if event.key == pygame.K_UP and grid[y-1][x] != 1 and grid[y-1][x] != 2:
                    player_pos = (x, y-1)
                elif event.key == pygame.K_DOWN and grid[y+1][x] != 1 and grid[y+1][x] != 2:
                    player_pos = (x, y+1)
                elif event.key == pygame.K_LEFT and grid[y][x-1] != 1 and grid[y][x-1] != 2:
                    player_pos = (x-1, y)
                elif event.key == pygame.K_RIGHT and grid[y][x+1] != 1 and grid[y][x+1] != 2:
                    player_pos = (x+1, y)
                elif event.key == pygame.K_SPACE: # Safe Path Request
                    path = bfs(grid, player_pos, end_pos)

        # Update player's location
        px, py = player_pos
        grid[py][px] = 3

        # Verify Win
        if player_pos == end_pos:
            print("I escaped successfully!🎉")
            running = False

        draw_grid(screen, grid, path)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
