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
        
def direction(x,y,ex,ey):
    val1,val2=-1,-1
    if ex-x>0:
        val1=1
    elif ex-x==0:
        val1=0
        
    if ey-y>0:
        val2=1
    elif ey-y==0:
        val2=0
        
    return val1,val2

def obstructed(x,y,ex,ey):
    global grid
    dir_X,dir_y=direction(x,y,ex,ey)
    print(dir_X,dir_y)
    stx,sty=x+dir_X,y+dir_y
    while(stx!=ex or sty!=ey):
        if(grid[stx][sty]!='  '):
            return False
        stx += dir_X  
        sty += dir_y 
    return True

def check():
    pass

def  check_mate():
    pass

def straight(x,y,ex,ey):
    if (x==ex or y==ey) and obstructed(x,y,ex,ey):
        return True
    return False

def diagonal(x,y,ex,ey):
    if (abs(x-ex)==abs(y-ey)) and obstructed(x,y,ex,ey):
        return True
    return False

def l_move(x,y,ex,ey):
    if (abs(x-ex),abs(y-ey)) in [(1,2),(2,1)]:
        return True
    return False

def movable(coin,x,y,ex,ey):
    color=coin[0]
    coin=coin[1]
    if(coin=='P'): #want to fix the bug
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
            return True
        else:
            print('Invalid move...Given end not reachable!!')
            return False 

def move():
    global turn
    if(turn):
        print("White's Move")
        x,y=map(int,input("Enter Start Point :").split(' '))
        ex,ey=map(int,input("Enter End Point :").split(' '))
        res=validate_move(x,y,ex,ey)
        if res:
            turn=0
    else:
        print("Black's Move")
        x,y=map(int,input("Enter Start Point :").split(' '))
        ex,ey=map(int,input("Enter End Point :").split(' '))
        res=validate_move(x,y,ex,ey)
        if res:
            turn=1

init_grid()
while(True):
    move()
    print_grid()
     