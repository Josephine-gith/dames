import pygame as pg
from random import randint
from collections import deque, namedtuple

# constantes utiles
NB_PIXELS =10
T_PIXELS =50
T_ECRAN = NB_PIXELS*T_PIXELS
RED = (255,0,0)
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
EPS=25
MARRON= (135,62,35)

# état initial du jeu

PIECES_B = 0

def case_to_coord(x,y):

# sous-fonctions utiles
def draw_damier():
    screen.fill(MARRON)
    for i in range(NB_PIXELS):
        for j in range(NB_PIXELS):
            if (i+j)%2==0:
                rect = pg.Rect(i*T_PIXELS, j*T_PIXELS, T_PIXELS, T_PIXELS)
                pg.draw.rect(screen, WHITE, rect)
           

def coups_possible(coord):
    X,Y=coord
    couleur = cases[(X,Y)][0] #la couleur de la pièce 1 =noir -1=blanc
    coups=[]
    if (X+couleur,Y+1) in cases.keys():
        if cases[X+couleur,Y+1][0]==couleur:
            1
        if cases[X+couleur*50,Y-50][0]==-couleur:
            coups.append((X+50*couleur,Y-50))
    

    





def draw_pieces():
    for i in range(NB_PIXELS):
        for j in range(NB_PIXELS):
            if j%2==1:
                pg.draw.circle( screen, BLACK, (i*T_PIXELS+25, j*T_PIXELS+25), 20)




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

def move_snake(snake, direction):
    for i in range(1,len(snake)):
        snake[-i]=snake[-i-1]
    snake[0]=Cell(x=snake[0][0]+direction[0],y=snake[0][1]+direction[1])
    return snake

def draw_snake(snake):
    for c in snake:
        rect_c = pg.Rect(c[0]*T_PIXELS, c[1]*T_PIXELS, T_PIXELS, T_PIXELS)
        pg.draw.rect(screen, GREEN, rect_c)

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
        draw_pieces

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
                if event.key == pg.K_q:
                    running = False 
        pg.display.update()

    pg.quit()
