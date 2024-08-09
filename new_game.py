import curses
import random 
stdscr = curses.initscr()
maxl = curses.LINES - 1 
maxc = curses.COLS
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.nodelay(True)
world = [] 
player_l = player_c = 0  
def init():
    global player_l , player_c
    for i in range(maxl):
        world.append([])
        for j in range(maxc):
            world[i].append(ord(" ") if random.random() > 0.03 else ord("."))
    player_l = random.randint(0,maxl)
    player_c = random.randint(0,maxc)
def in_range(a,min,max):
    if a < min :
        return min 
    if a > max :
        return max
    return a 



def move(c):
    global player_l , player_c
    if c == "w":
        player_l -= 1 
    elif c == "s":
        player_l += 1
    elif c == "a":
        player_c -= 1
    elif c == "d":
        player_c += 1 
    player_l = in_range(player_l , 0,maxl)
    player_c = in_range(player_c ,0,maxc)




def draw():
    for i in range(maxl):
        for j in range(maxc):
            stdscr.addch(i, j, world[i][j])
    stdscr.addch(player_l, player_c, ord("x"))
    stdscr.refresh()
init()
playing = True 
while playing:
    try :
        c = stdscr.getkey()
    except :
        c = ""
    if c in 'asdw':
        move(c)
    elif c == 'q':
        playing = False
    draw()


stdscr.clear()
stdscr.refresh()
