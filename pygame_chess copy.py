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
first_click = True
move_is_legal = False
whites_turn = 1 

running = True
screen = pygame.display.set_mode((400, 400))
caption = 'Chess Game'
pygame.display.set_caption(caption)

pos = [
    ['a1', 'rw'], ['a2', 'pw'], ['a3', '//'], ['a4','//'], ['a5','//'], ['a6','//'], ['a7','pb'], ['a8','rb'],
    ['b1', 'kw'], ['b2', 'pw'], ['b3', '//'], ['b4','//'], ['b5','//'], ['b6','//'], ['b7','pb'], ['a8','kb'],
    ['c1', 'bw'], ['c2', 'pw'], ['c3', '//'], ['c4','//'], ['c5','//'], ['c6','//'], ['c7','pb'], ['c8','bb'],
    ['d1', 'qw'], ['d2', 'pw'], ['d3', '//'], ['d4','//'], ['d5','//'], ['d6','//'], ['d7','pb'], ['d8','qb'],
    ['e1', 'Kw'], ['e2', 'pw'], ['e3', '//'], ['e4','//'], ['e5','//'], ['e6','//'], ['e7','pb'], ['e8','Kb'],
    ['f1', 'bw'], ['f2', 'pw'], ['f3', '//'], ['f4','//'], ['f5','//'], ['f6','//'], ['f7','pb'], ['f8','bb'],
    ['g1', 'kw'], ['g2', 'pw'], ['g3', '//'], ['g4','//'], ['g5','//'], ['g6','//'], ['g7','pb'], ['g8','kb'],
    ['h1', 'rw'], ['h2', 'pw'], ['h3', '//'], ['h4','//'], ['h5','//'], ['h6','//'], ['h7','pb'], ['h8','rb']
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
        if piece[1] == 'rw':
            screen.blit(rw, notation[position[count]])
        elif piece[1] == 'rb':
            screen.blit(rb, notation[position[count]])
        elif piece[1] == 'kw':
            screen.blit(kw, notation[position[count]])
        elif piece[1] == 'kb':
            screen.blit(kb, notation[position[count]])
        elif piece[1] == 'bw':
            screen.blit(bw, notation[position[count]])
        elif piece[1] == 'bb':
            screen.blit(bb, notation[position[count]])
        elif piece[1] == 'qw':
            screen.blit(qw, notation[position[count]])
        elif piece[1] == 'qb':
            screen.blit(qb, notation[position[count]])
        elif piece[1] == 'Kw':
            screen.blit(Kw, notation[position[count]])
        elif piece[1] == 'Kb':
            screen.blit(Kb, notation[position[count]])
        elif piece[1] == 'pw':
            screen.blit(pw, notation[position[count]])
        elif piece[1] == 'pb':
            screen.blit(pb, notation[position[count]])
        elif piece[1] == '//':
            continue

def update_pos(old_pos, new_pos):
    global pos
    pos[pos.index(new_pos)][1] = pos[pos.index(old_pos)][1]
    pos[pos.index(old_pos)][1] = '//'
    

def legal_moves(chess_piece):
    if chess_piece[1] == 'p': 
        move_is_legal = True
    elif chess_piece[1] == 'r':
        move_is_legal = True
    elif chess_piece[1] == 'b':
        move_is_legal = True
    elif chess_piece[1] == 'k':
        move_is_legal = True
    elif chess_piece[1] == 'q':
        move_is_legal = True
    elif chess_piece[1] == 'K':
        move_is_legal = True

        
        
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

                    elif mouse_inputs[0] and first_click:
                        original_pos = pos[position.index(sqr)]
                        if (whites_turn == 1 and original_pos[1][1] == 'w') or (whites_turn == -1 and original_pos[1][1] == 'b'):
                            first_click = False
                            whites_turn = whites_turn * -1


                    elif mouse_inputs[0] and first_click == False:
                        new_pos = pos[position.index(sqr)]
                        if new_pos == original_pos:
                            first_click = False
                        else: 
                            print('From', original_pos, 'to', new_pos)
                            first_click = True
                            update_pos(original_pos, new_pos)
        place_board()   
        place_pieces()         
    pygame.display.update()

pygame.quit()