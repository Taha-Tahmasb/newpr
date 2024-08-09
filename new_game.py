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
food = []
score = 0 
player_l = player_c = 0  
def random_place():
    a = random.randint(0,maxl) 
    b = random.randint(0,maxc)
    while world[a][b] != ord(" "):
        a = random.randint(0,maxl) 
        b = random.randint(0,maxc)
    return a,b 
        

def init():
    global player_l , player_c
    for i in range(-1 , maxl + 1):
        world.append([])
        for j in range(-1, maxc + 1):
            world[i].append(ord(" ") if random.random() > 0.03 else ord("."))
    player_l , player_c = random_place()
    for i in range(10):
        fl ,fc = random_place()
        fa = random.randint(1000,10000)
        food.append((fl,fc,fa))

def in_range(a,min,max):
    if a < min :
        return min 
    if a > max :
        return max
    return a 



def move(c):
    global player_l , player_c
    if c == "w" and world[player_l - 1][player_c] != ord("."):
        player_l -= 1 
    elif c == "s" and world[player_l + 1][player_c] != ord("."):
        player_l += 1
    elif c == "a" and world[player_l][player_c - 1] != ord("."):
        player_c -= 1
    elif c == "d" and world[player_l][player_c + 1] != ord("."):
        player_c += 1 
    player_l = in_range(player_l , 0,maxl - 1)
    player_c = in_range(player_c ,0,maxc - 1)

def check_food():
    global food , score
    for f in food :
        fl , fc , fa = f
        if fl == player_l and fc == player_c :
            score += 10 
            food.remove(f)
            world[fl][fc] = ord(" ")
            fa = random.randint(1000,10000)
            food.append((fl,fc,fa))


def draw():
    for i in range(maxl):
        for j in range(maxc):
            stdscr.addch(i, j, world[i][j])
    for c in food:
        fl , fc , fa = c
        stdscr.addch(fl, fc, "🍎")
    stdscr.addch(player_l, player_c, "🚀")
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
    check_food()
    draw()


stdscr.clear()
stdscr.refresh()
