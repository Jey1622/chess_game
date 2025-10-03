grid=[(['  ']*8)[:] for x in range(8)]
turn =1 #1 means white move, 0 means black move

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

def straight(x,y,ex,ey):
    if x==ex or y==ey:
        return True
    return False

def diagonal(x,y,ex,ey):
    if x-ex==y-ey:
        return True
    return False

def l_move(x,y,ex,ey):
    if (abs(x-ex),abs(y-ey)) in [(1,3),(3,1)]:
        return True
    return False

def movable(coin,x,y,ex,ey):
    color=coin[0]
    coin=coin[1]
    if(coin=='P'):
        if straight(x,y,ex,ey) or diagonal(x,y,ex,ey) and abs(x-ex)==1 and abs(y-ey)<=1:
            if color=='B' and ex>x:
                return True
            elif color=='W' and ex<x:
                return True
            else :
                return False
    elif(coin=='Q'):
        if straight(x,y,ex,ey) or diagonal(x,y,ex,ey):
            return True
        return False
    elif (coin=='R'):
        if straight(x,y,ex,ey):
            return True
        return False
    elif (coin=='B'):
        if diagonal(x,y,ex,ey):
            return True
        return False
    elif (coin=='H'):
        if l_move(x,y,ex,ey):
            return True
        return False
    elif (coin=='K'):
        if (straight(x,y,ex,ey) or diagonal(x,y,ex,ey)) and (abs(x-ex)<=1 and abs(y-ey)<=1):
            return True
        return False
    

    else:
        return False
    

def validate_move(x,y,ex,ey):
    global turn,grid
    coin=grid[x][y]
    end_coin=grid[ex][ey]

    if coin=='  ' or (turn==1 and (coin[0]=='B' or end_coin[0]=='W')) or (turn==0 and (coin[0]=='W' or end_coin[0]=='B')):
        return False
    else:
        res=movable(coin,x,y,ex,ey)

        if res is True:
            grid[ex][ey]=coin
            grid[x][y]='  '
        else:
            print('Invalid move...Given end not reachable!!')

def move():
    global turn
    if(turn):
        print("White's Move")
        x,y=map(int,input("Enter Start Point :").split(' '))
        ex,ey=map(int,input("Enter End Point :").split(' '))
        res=validate_move(x,y,ex,ey)
        turn=0
    else:
        print("Black's Move")
        x,y=map(int,input("Enter Start Point :").split(' '))
        ex,ey=map(int,input("Enter End Point :").split(' '))
        res=validate_move(x,y,ex,ey)
        turn=1

init_grid()
while(True):
    move()
    print_grid()
     