import pygame as pg

print("hello")
# Constantes utiles
NB_PIXELS = 10
T_PIXELS = 50
T_ECRAN = NB_PIXELS * T_PIXELS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MARRON = (135, 62, 35)
BEIGE = (247, 222, 166)
RAYON = 20

# État initial du jeu
Cases = {}
for i in range(NB_PIXELS):
    for j in range(NB_PIXELS):
        if (i + j) % 2 == 1:
            if j in range(4):
                Cases[(i, j)] = BLACK
            elif j in range(6, NB_PIXELS):
                Cases[(i, j)] = WHITE
            else:
                Cases[(i, j)] = None


# Fonctions d'affichage
def draw_damier():
    screen.fill(MARRON)
    for i in range(NB_PIXELS):
        for j in range(NB_PIXELS):
            if (i + j) % 2 == 0:
                rect = pg.Rect(i * T_PIXELS, j * T_PIXELS, T_PIXELS, T_PIXELS)
                pg.draw.rect(screen, BEIGE, rect)


def draw_pieces():
    for coord in Cases.keys():
        if Cases[coord]:
            pg.draw.circle(
                screen,
                Cases[coord],
                (coord[0] * T_PIXELS + 25, coord[1] * T_PIXELS + 25),
                RAYON,
            )


def update_plateau(plateau, coord_i, coord_f):
    if legit_move(plateau, coord_i, coord_f):
        couleur = plateau[coord_i]
        plateau[coord_i] = None
        plateau[coord_f] = couleur
    else:
        None


def get_coordinates():
    print("Cliquez sur une case pour sélectionner une pièce.")
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                return (x // T_PIXELS, y // T_PIXELS)


# Règles de déplacement
def legit_move(plateau, coord_i, coord_f):
    global tour
    couleur = plateau[coord_i]
    if plateau[coord_f] is None and ((coord_f[0] + coord_f[1]) % 2) == 1:
        if couleur == WHITE and tour%2==0:
            if (coord_f[1] - coord_i[1]) == -1 and abs(coord_f[0] - coord_i[0]) == 1:
                tour+=1
                return True
            elif abs(coord_f[1] - coord_i[1]) == 2 and abs(coord_f[0] - coord_i[0]) == 2:
                if plateau[(coord_f[0]+coord_i[0])/2,(coord_f[1]+coord_i[1])/2] == BLACK:
                    plateau[(coord_f[0]+coord_i[0])/2,(coord_f[1]+coord_i[1])/2] = None
                    return True
            else:
                return False
        if couleur == BLACK and tour%2==1:
            if (coord_i[1] - coord_f[1]) == -1 and abs(coord_f[0] - coord_i[0]) == 1:
                tour+=1
                return True
            elif abs(coord_f[1] - coord_i[1])== 2 and abs(coord_f[0] - coord_i[0]) == 2:
                if plateau[(coord_f[0]+coord_i[0])/2,(coord_f[1]+coord_i[1])/2] == WHITE:
                    plateau[(coord_f[0]+coord_i[0])/2,(coord_f[1]+coord_i[1])/2] = None
                    return True
            else:
                return False
    else:
        return False

def joueur(tour):
    if tour%2==0:
        return "Blancs"
    else:
        return "Noirs"   
    

# Boucle principale
if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((T_ECRAN, T_ECRAN))
    clock = pg.time.Clock()
    running = True
    tour = 0
    draw_damier()
    draw_pieces()
    pg.display.update()

    while running:
        clock.tick(10)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    running = False
            
        
        print(f"C'est aux {joueur(tour)} de jouer.")
        print("Sélectionnez la pièce à déplacer.")
        coord_i = get_coordinates()
        print("Sélectionnez la case de destination.")
        coord_f = get_coordinates()

        if coord_i not in Cases or coord_f not in Cases:
            print("Coordonnées invalides.")
            continue
        else:
            update_plateau(Cases, coord_i, coord_f)

        draw_damier()
        draw_pieces()
        pg.display.update()

    pg.quit()
