grid=[(['.']*8)[:] for x in range(8)]
turn = 1  # 1 means white move, 0 means black move

# W-white B-black
# K-king Q-queen H-knight B-Bishop R-Rook P-pawn

# initiating chess grid
def init_grid():
    arr = ['R', 'H', 'B', 'K', 'Q', 'B', 'H', 'R']

    for x in range(8):  # align black power coins
        grid[0][x] = 'B' + arr[x]

    for x in range(8):  # align white power coins
        grid[-1][x] = 'W' + arr[x]

    for x in range(8):  # align black pawns coins
        grid[1][x] = 'BP'

    for x in range(8):  # align white pawns coins
        grid[-2][x] = 'WP'


def print_grid():
    global grid
    for x in grid:
        print(x)


def direction(x, y, ex, ey):
    val1, val2 = -1, -1
    if ex - x > 0:
        val1 = 1
    elif ex - x == 0:
        val1 = 0

    if ey - y > 0:
        val2 = 1
    elif ey - y == 0:
        val2 = 0

    return val1, val2


def obstructed(x, y, ex, ey):
    global grid
    dir_X, dir_y = direction(x, y, ex, ey)
    stx, sty = x + dir_X, y + dir_y
    while (stx != ex or sty != ey):
        if (grid[stx][sty] != '.'):
            return False
        stx += dir_X
        sty += dir_y
    return True


def check(bx=-1, by=-1, wx=-1, wy=-1, mode='D'):
    global grid
    WCheck, BCheck = False, False
    if (bx, by, wx, wy) == (-1, -1, -1, -1):
        for x in range(8):
            for y in range(8):
                if grid[x][y] == 'BK':
                    bx, by = x, y
                if grid[x][y] == 'WK':
                    wx, wy = x, y

    # Check if White King is in check (attacked by black pieces)
    if wx >= 0:
        for x in range(8):
            for y in range(8):
                if grid[x][y] != '.' and grid[x][y][0] == 'B':
                    if movable(grid[x][y], x, y, wx, wy):
                        WCheck = True

    # Check if Black King is in check (attacked by white pieces)
    if bx >= 0:
        for x in range(8):
            for y in range(8):
                if grid[x][y] != '.' and grid[x][y][0] == 'W':
                    if movable(grid[x][y], x, y, bx, by):
                        BCheck = True

    if mode == 'D':
        return ((wx, wy), (bx, by), WCheck, BCheck)
    elif mode == 'W':
        return WCheck
    elif mode == 'B':
        return BCheck


def check_mate():
    global grid
    a = check()
    wx, wy = a[0]
    bx, by = a[1]
    Wc, Bc = a[2], a[3]
    if Wc:
        for x in [0, 1, -1]:
            for y in [0, 1, -1]:
                if wx + x in range(8) and wy + y in range(8) and grid[wx + x][wy + y] == '.':
                    a = check(wx + x, wy + y, -1, -1, mode='W')
                    if a == False:
                        return False, 1
        print("Check mate for White")
        return (True, 'W')
    elif Bc:
        for x in [0, 1, -1]:
            for y in [0, 1, -1]:
                if bx + x in range(8) and by + y in range(8) and grid[bx + x][by + y] == '.':
                    a = check(-1, -1, bx + x, by + y, mode='B')
                    if a == False:
                        return False, 1
        print("Check mate for Black")
        return (True, 'B')
    else:
        return False, 1


def straight(x, y, ex, ey):
    if (x == ex or y == ey) and obstructed(x, y, ex, ey):
        return True
    return False


def diagonal(x, y, ex, ey):
    if (abs(x - ex) == abs(y - ey)) and obstructed(x, y, ex, ey):
        return True
    return False


def l_move(x, y, ex, ey):
    if (abs(x - ex), abs(y - ey)) in [(1, 2), (2, 1)]:
        return True
    return False


def movable(coin, x, y, ex, ey):
    global grid
    color = coin[0]
    coin = coin[1]
    
    if (coin == 'P'):
        # Pawn forward movement (straight)
        if color == 'B' and ex > x:
            if y == ey and grid[ex][ey] == '.':  # Move forward only if empty
                if ex - x == 1:  # Single step
                    return True
                elif ex - x == 2 and x == 1 and grid[x + 1][y] == '.':  # Double step from start
                    return True
        elif color == 'W' and ex < x:
            if y == ey and grid[ex][ey] == '.':  # Move forward only if empty
                if x - ex == 1:  # Single step
                    return True
                elif x - ex == 2 and x == 6 and grid[x - 1][y] == '.':  # Double step from start
                    return True
        
        # Pawn diagonal capture
        if abs(y - ey) == 1 and abs(x - ex) == 1 and grid[ex][ey] != '.':
            if color == 'B' and ex > x:
                return True
            elif color == 'W' and ex < x:
                return True
        
        return False
    
    elif (coin == 'Q'):
        if straight(x, y, ex, ey) or diagonal(x, y, ex, ey):
            return True
        return False
    elif (coin == 'R'):
        if straight(x, y, ex, ey):
            return True
        return False
    elif (coin == 'B'):
        if diagonal(x, y, ex, ey):
            return True
        return False
    elif (coin == 'H'):
        if l_move(x, y, ex, ey):
            return True
        return False
    elif (coin == 'K'):
        if (straight(x, y, ex, ey) or diagonal(x, y, ex, ey)) and (abs(x - ex) <= 1 and abs(y - ey) <= 1):
            return True
        return False
    else:
        return False


def validate_move(gr, t, x, y, ex, ey):
    global turn, grid
    turn = t
    grid = gr
    coin = grid[x][y]
    end_coin = grid[ex][ey]

    # Check if empty square selected or wrong turn
    if coin == '.':
        return False
    
    # Turn 0 = Black's turn, Turn 1 = White's turn
    if turn == 0 and coin[0] != 'B':
        return False
    if turn == 1 and coin[0] != 'W':
        return False
    
    # Can't capture own piece
    if end_coin != '.' and end_coin[0] == coin[0]:
        return False

    res = movable(coin, x, y, ex, ey)

    if res is True:
        return True
    else:
        return False


def move():
    turn = 0
    if (turn):
        print("White's Move")
        x, y = map(int, input("Enter Start Point :").split(' '))
        ex, ey = map(int, input("Enter End Point :").split(' '))
        res = validate_move(x, y, ex, ey)
        turn = 0
    else:
        print("Black's Move")
        x, y = map(int, input("Enter Start Point :").split(' '))
        ex, ey = map(int, input("Enter End Point :").split(' '))
        res = validate_move(x, y, ex, ey)
        turn = 1


def set_grid(gr):
    global grid
    grid = gr