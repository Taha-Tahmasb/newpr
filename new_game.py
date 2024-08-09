import curses
stdscr = curses.initscr()
maxl = curses.LINES - 1 
maxc = curses.COLS
curses.noecho()
curses.cbreak()
stdscr.keypad(True)


world = [] 
def init():
    for i in range(maxl):
        world.append([])
        for j in range(maxc):
            world[i].append(ord("."))
def draw():
    for i in range(maxl):
        for j in range(maxc):
            stdscr.addch(i, j, world[i][j])
    stdscr.refresh()
init()
draw()

stdscr.refresh()
stdscr.getkey()