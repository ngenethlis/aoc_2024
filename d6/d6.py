


def parse(infile = 'input.txt'):
    lines = open(infile, 'r').readlines()
    GRID = [list(l.strip()) for l in lines]
    return GRID

def find_position(grid, target='^'):
    # Iterate through the grid to locate the target character
    for row_idx, row in enumerate(grid):
        if target in row:  # Check if target exists in the current row
            col_idx = row.index(target)  # Find the column index
            return row_idx, col_idx  # Return the position as (row, col)

def print_grid(G):
    for row in G:
        print("".join(row))


def traverse_grid(G):
    pos = find_position(G)
    distinct = set()
    r,c = pos[0],pos[1]
    print(f'pos is {pos}')
    dir = 'UP'
    while 0<=r<len(G) and 0<=c<len(G[r]):
        G[r][c] = 'X'
        if dir == 'UP':
            print("dir is UP")
            if 0<=r-1 and G[r-1][c] =='#':
                print("changing to Right")
                dir = 'RIGHT'
            else:
                r-=1
        elif dir=='RIGHT':
            print('dir is right')
            if c+1<len(G[r]) and G[r][c+1] =='#':
                dir = 'DOWN'
            else:
                c+=1
        elif dir=='DOWN':
            if r+1<len(G) and G[r+1][c] == '#':
                dir = 'LEFT'
            else:
                r+=1
        elif dir=='LEFT':
            if 0<=c-1 and G[r][c-1] == '#':
                dir = 'UP'
            else:
                c-=1
        else:
            print(f'ERROR at pos {r},{c}')

        if 0 <= r < len(G) and 0 <= c < len(G[r]):
            G[r][c] = '^'
            distinct.add((r, c))
            print(f'{r}, {c}, {dir}')
        print(f'{r},{c},{dir}')
        distinct.add(tuple((r,c)))
    print_grid(G)
    return distinct #p2
    # return len(distinct) #p1

def is_guard_stuck_in_loop(G,sp):
    pos = sp  # Assuming this function finds the guard's starting position
    visited = set()  # To store (position, direction) pairs
    r, c = pos[0],pos[1]
    dir = 'UP'
    
    while 0 <= r < len(G) and 0 <= c < len(G[r]):
        # Add the current state (position and direction) to the visited set
        state = (r, c, dir)
        if state in visited:
            print(f"Guard is stuck in a loop at {state}")
            return True
        visited.add(state)

        # Simulate movement
        if dir == 'UP':
            if r - 1 >= 0 and G[r - 1][c] == '#':
                dir = 'RIGHT'
            else:
                r -= 1
        elif dir == 'RIGHT':
            if c + 1 < len(G[r]) and G[r][c + 1] == '#':
                dir = 'DOWN'
            else:
                c += 1
        elif dir == 'DOWN':
            if r + 1 < len(G) and G[r + 1][c] == '#':
                dir = 'LEFT'
            else:
                r += 1
        elif dir == 'LEFT':
            if c - 1 >= 0 and G[r][c - 1] == '#':
                dir = 'UP'
            else:
                c -= 1
        else:
            print(f"Unexpected direction: {dir}")
            break

    #print("Guard is not stuck in a loop")
    return False


    return len(obs)

def place_obstacles(distinct, G, sp):
    obs = set()
    distinct.discard(sp)  # Safe removal without error if sp isn't in distinct

    for (r, c) in distinct:
        if 0 <= r < len(G) and 0 <= c < len(G[r]):
            # Create a copy of the grid for testing
            mod_G = [row[:] for row in G]  # Deep copy of the grid
            mod_G[r][c] = '#'  # Place obstacle at (r, c)

            # Check if placing the obstacle causes the guard to get stuck in a loop
            if is_guard_stuck_in_loop(mod_G, sp):
                obs.add((r, c))

    return len(obs)




def main():
    G = parse()
    start_pos = find_position(G)
    distinict = traverse_grid(G)
    r = place_obstacles(distinict,G,start_pos)
    print(r)

main()