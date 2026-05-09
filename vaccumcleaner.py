import random

# Setup grid
size = 5
grid = [[random.random() < 0.3 for _ in range(size)] for _ in range(size)]
row, col = 0, 0
steps, cleaned = 0, 0
total_dirt = sum(sum(row) for row in grid)

print(f"Dirt to clean: {total_dirt}\n")

# Simple reflex agent loop
while total_dirt > 0 and steps < 100:
    steps += 1
    
    # Display current state
    for r in range(size):
        for c in range(size):
            if r == row and c == col:
                print("A", end=" ")
            else:
                print("D" if grid[r][c] else ".", end=" ")
        print()
    print(f"Step: {steps} | Cleaned: {cleaned}/{total_dirt}\n")
    
    # Simple reflex rule: if dirty -> clean, else -> move randomly
    if grid[row][col]:
        grid[row][col] = False
        cleaned += 1
        print("CLEANED!\n")
    else:
        # Random movement
        dr, dc = random.choice([(-1,0), (1,0), (0,-1), (0,1)])
        new_r, new_c = row + dr, col + dc
        if 0 <= new_r < size and 0 <= new_c < size:
            row, col = new_r, new_c
            print(f"Moved to ({row},{col})\n")

print(f"\nDone! Cleaned {cleaned} dirt in {steps} steps")