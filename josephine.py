import pygame as pg

# constantes utiles
NB_PIXELS =10
T_PIXELS =50
T_ECRAN = NB_PIXELS*T_PIXELS
BLACK=(0,0,0)
WHITE=(255,255,255)
MARRON=(135,62,35)
BEIGE=(247,222,166)
RAYON = 20

# état initial du jeu

Cases = {}
for i in range(NB_PIXELS):
    for j in range(NB_PIXELS):
        if (i+j)%2==1:
            if j in range(4):
                Cases[(i,j)] = BLACK
            elif j in range(6,NB_PIXELS):
                Cases[(i,j)] = WHITE
            else :
                Cases[(i,j)] = None

# sous-fonctions utiles
def draw_damier():
    screen.fill(MARRON)
    for i in range(NB_PIXELS):
        for j in range(NB_PIXELS):
            if (i+j)%2==0:
                rect = pg.Rect(i*T_PIXELS, j*T_PIXELS, T_PIXELS, T_PIXELS)
                pg.draw.rect(screen, BEIGE, rect)

def draw_pieces():
    for coord in Cases.keys():
        if Cases[coord]!= None :
            pg.draw.circle(screen, Cases[coord], (coord[0]*T_PIXELS+25,coord[1]*T_PIXELS+25), RAYON)

'''
def handle_event(event, running, direction):
    if event.type == pg.QUIT:
        running = False
    # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
    elif event.type == pg.KEYDOWN:
        # si la touche est "Q" on veut quitter le programme
        if event.key == pg.K_q:
            running = False
        if event.key == pg.K_UP and direction!=Cell(x=0,y=1):
            direction=Cell(x=0,y=-1)
        if event.key == pg.K_DOWN and direction!=Cell(x=0,y=-1):
            direction=Cell(x=0,y=1)
        if event.key == pg.K_LEFT and direction!=Cell(x=1,y=0):
            direction=Cell(x=-1,y=0)
        if event.key == pg.K_RIGHT and direction!=Cell(x=-1,y=0):
            direction=Cell(x=1,y=0)
    return running, direction

def game_over(snake, running):
    if snake[-1] in list(snake)[:-2]:
        running = False
    elif snake[0][0] in [-1,NB_PIXELS] or snake[0][-1] in [-1,NB_PIXELS]:
        running = False
    return running
'''

if __name__ == "__main__":
    #initialisation de l'écran
    pg.init()
    screen = pg.display.set_mode((T_ECRAN, T_ECRAN))
    clock = pg.time.Clock()

    running = True
    while running:
        clock.tick(1)

        draw_damier()
        draw_pieces()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
                if event.key == pg.K_q:
                    running = False 
        
        pg.display.update()

    pg.quit()