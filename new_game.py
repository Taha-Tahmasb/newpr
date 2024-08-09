import curses
import random 
stdscr = curses.initscr()
maxl = curses.LINES - 1 
maxc = curses.COLS
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
curses.nodelay( True)


world = [] 
player_1 = player_c = 0  
def init():
    global player_1 , player_c
    for i in range(maxl):
        world.append([])
        for j in range(maxc):
            world[i].append(ord(" ") if random.random() > 0.03 else ord("."))
    player_1 = random.randint(0,maxl)
    player_c = random.randint(0,maxc)
def move(c):
    pass



def draw():
    for i in range(maxl):
        for j in range(maxc):
            stdscr.addch(i, j, world[i][j])
    stdscr.addch(player_1, player_c, ord("x"))
    stdscr.refresh()
init()
playing = True 
while playing:
    c = stdscr.getkey()
    if c in ['asdw']:
        move(c)
    elif c == 'q':
        playing = False



    draw()


stdscr.getkey()