import pygame
from pygame.locals import * 

pygame.init()

#Globale variabler
pw = 0 
pb = 0 
kw = 0 
kb = 0 
bw = 0 
bb = 0 
rw = 0 
rb = 0 
qw = 0 
qb = 0 
Kw = 0 
Kb = 0
position = []
notation = []
sqr_size = 50

running = True
screen = pygame.display.set_mode((400, 400))
caption = 'Chess Game'
pygame.display.set_caption(caption)

pos = [
    'rw', 'pw', '//', '//', '//', '//', 'pb', 'rb', #a rekke
    'kw', 'pw', '//', '//', '//', '//', 'pb', 'kb', #b rekke
    'bw', 'pw', '//', '//', '//', '//', 'pb', 'bb', #c rekke
    'qw', 'pw', '//', '//', '//', '//', 'pb', 'qb', #d rekke
    'Kw', 'pw', '//', '//', '//', '//', 'pb', 'Kb', #e rekke
    'bw', 'pw', '//', '//', '//', '//', 'pb', 'bb', #f rekke
    'kw', 'pw', '//', '//', '//', '//', 'pb', 'kb', #g rekke
    'rw', 'pw', '//', '//', '//', '//', 'pb', 'rb', #h rekke
    ] 

def make_notation():
    global notation, sqr_size

    sqr_size = 50 
    notation_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    count = 0
    notation = {}
    for notation_letter in notation_letters:
        for notation_nr in range (1, 9):
            notation[str(notation_letter) + str(notation_nr)] = [sqr_size * count, sqr_size * (notation_nr -1)]
        count += 1
        


def load_pieces():
    global pw, pb, kw, kb, bw, bb, rw, rb, qw, qb, Kw, Kb
    Kw = pygame.image.load('whiteKing.png')
    qw = pygame.image.load('whiteQueen.png')
    rw = pygame.image.load('whiteRook.png')
    bw = pygame.image.load('whiteBishop.png')
    kw = pygame.image.load('whiteKnight.png')
    pw = pygame.image.load('whitePawn.png')

    Kb = pygame.image.load('blackKing.png')
    qb = pygame.image.load('blackQueen.png')
    rb = pygame.image.load('blackRook.png')
    bb = pygame.image.load('blackBishop.png')
    kb = pygame.image.load('blackKnight.png')
    pb = pygame.image.load('blackPawn.png')


def place_board():
    rows = 7 
    rows_placed = 0

    next_tile = 1
    rect_size = 50
    while rows_placed <= rows:
        for square in range(0, 8):
            if next_tile == 1:
                rect_color = (255, 178, 102)
            else:
                rect_color = (85, 30, 0)
            pygame.draw.rect(screen, rect_color, pygame.Rect(rect_size * square, rect_size * rows_placed, rect_size, rect_size))
            next_tile = next_tile * -1
        rows_placed += 1
        next_tile = next_tile * -1


def place_pieces():
    global position
    count = -1
    position = list(notation)
    for piece in pos:
        count += 1
        if piece == 'rw':
            screen.blit(rw, notation[position[count]])
        elif piece == 'rb':
            screen.blit(rb, notation[position[count]])
        elif piece == 'kw':
            screen.blit(kw, notation[position[count]])
        elif piece == 'kb':
            screen.blit(kb, notation[position[count]])
        elif piece == 'bw':
            screen.blit(bw, notation[position[count]])
        elif piece == 'bb':
            screen.blit(bb, notation[position[count]])
        elif piece == 'qw':
            screen.blit(qw, notation[position[count]])
        elif piece == 'qb':
            screen.blit(qb, notation[position[count]])
        elif piece == 'Kw':
            screen.blit(Kw, notation[position[count]])
        elif piece == 'Kb':
            screen.blit(Kb, notation[position[count]])
        elif piece == 'pw':
            screen.blit(pw, notation[position[count]])
        elif piece == 'pb':
            screen.blit(pb, notation[position[count]])
        elif piece == '//':
            continue


load_pieces() 
make_notation()
place_board()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        mouse_pos = pygame.mouse.get_pos()
        mouse_inputs = pygame.mouse.get_pressed()
        highlight_sqr_color = (200, 0 ,0 )

        for sqr in position:
                sqr_cordinates = notation[sqr]
                if (mouse_pos[0] >= sqr_cordinates[0] and mouse_pos[0] <= (sqr_cordinates[0] + sqr_size)) and (mouse_pos[1] >= sqr_cordinates[1] and mouse_pos[1] <= (sqr_cordinates[1] + sqr_size)):
                    if mouse_inputs[2]: 
                        pygame.draw.rect(screen, highlight_sqr_color, pygame.Rect(notation[sqr],(sqr_size, sqr_size)))

                    elif mouse_inputs[0]:
                        print(pos[position.index(sqr)])
                        print(pos.index(pos[position.index(sqr)]))
        place_pieces()            
    pygame.display.update()

pygame.quit()