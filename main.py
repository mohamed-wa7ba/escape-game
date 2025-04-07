import random
import time

# Game constants
WALL = '▓'  # Wall character
PATH = ' '  # Empty path
PLAYER = 'P'  # Player character
GUARD = 'G'  # Guard character
EXIT = 'E'  # Exit character
TRAIL = '·'  # Path suggestion marker

# Maze dimensions
WIDTH = 15
HEIGHT = 10

def create_prison():
    """Create a prison maze with walls, player, exit, and guards"""
    # Initialize empty prison
    prison = [[PATH for _ in range(WIDTH)] for _ in range(HEIGHT)]

    # Create border walls
    for i in range(WIDTH):
        prison[0][i] = WALL
        prison[HEIGHT-1][i] = WALL
    for i in range(HEIGHT):
        prison[i][0] = WALL
        prison[i][WIDTH-1] = WALL

    # Place player at top-left corner
    prison[1][1] = PLAYER

    # Place exit at bottom-right corner
    prison[HEIGHT-2][WIDTH-2] = EXIT

    # Place guards randomly
    guards = 5
    while guards > 0:
        x, y = random.randint(1, WIDTH-2), random.randint(1, HEIGHT-2)
        if prison[y][x] == PATH:
            prison[y][x] = GUARD
            guards -= 1

    return prison

def print_prison(prison):
    """Print the prison layout"""
    for row in prison:
        print(' '.join(row))
    print()

def simple_pathfinder(prison, start, end):
    """
    Simple pathfinding algorithm using 'right-hand rule' maze solving
    Returns a path from start to end (may not be optimal)
    """
    x, y = start
    path = []

    # Movement directions (right, down, left, up)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dir_idx = 0  # Start with right direction

    for _ in range(100):  # Maximum attempts
        path.append((x, y))

        if (x, y) == end:
            return path

        # Try to move in current direction
        dx, dy = directions[dir_idx]
        nx, ny = x + dx, y + dy

        if prison[ny][nx] in (PATH, EXIT):
            x, y = nx, ny
        else:
            # Change direction if can't move
            dir_idx = (dir_idx + 1) % 4

    return path  # May not reach the goal

def main():
    """Main game loop"""
    prison = create_prison()
    player_pos = (1, 1)
    exit_pos = (WIDTH-2, HEIGHT-2)

    while True:
        # Display prison
        print_prison(prison)

        # Check win condition
        if player_pos == exit_pos:
            print("🎉 Congratulations! You escaped the prison!")
            break

        # Get player input
        move = input("Use WASD to move, or SPACE to show path: ").lower()

        if move == ' ':
            # Show suggested path
            path = simple_pathfinder(prison, player_pos, exit_pos)
            for x, y in path[1:]:  # Skip current player position
                if prison[y][x] == PATH:
                    prison[y][x] = TRAIL
            print_prison(prison)
            input("Press Enter to continue...")
            # Clear path markers
            for x, y in path[1:]:
                if prison[y][x] == TRAIL:
                    prison[y][x] = PATH
            continue

        # Process movement
        dx, dy = 0, 0
        if move == 'w': dy = -1  # Up
        elif move == 's': dy = 1  # Down
        elif move == 'a': dx = -1  # Left
        elif move == 'd': dx = 1  # Right
        else:
            print("Use W for up, S for down, A for left, D for right")
            continue

        # Validate movement
        new_x, new_y = player_pos[0] + dx, player_pos[1] + dy
        if prison[new_y][new_x] == WALL:
            print("Can't walk through walls!")
            continue
        elif prison[new_y][new_x] == GUARD:
            print("💀 You hit a guard! Game over!")
            break

        # Update player position
        prison[player_pos[1]][player_pos[0]] = PATH
        player_pos = (new_x, new_y)
        prison[player_pos[1]][player_pos[0]] = PLAYER

if __name__ == "__main__":
    main()
