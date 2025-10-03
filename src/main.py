grid=[(['.']*8)[:] for x in range(8)];
# print(grid)

#W-white B-black
#K-king Q-queen H-knight B-Bishop R-Rook P-pawn

#initiating chess grid
def init_grid():
    arr=['R','H','B','K','Q','B','H','R']

    for x in range(8): #align black power coins
        grid[0][x]='B'+arr[x]

    for x in range(8): #align white power coins
        grid[-1][x]='W'+arr[x]

    for x in range(8): #align black pawns coins
        grid[1][x]='BP'

    for x in range(8): #align white pawns coins
        grid[-2][x]='WP'


def print_grid():
    global grid
    for x in grid:
        print(x)

init_grid()
print_grid()