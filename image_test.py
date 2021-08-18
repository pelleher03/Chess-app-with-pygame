import pygame 

pygame.init()
running = True

screen = pygame.display.set_mode((600, 600))
white = (0, 0, 255)
pawn = pygame.image.load('whitepawn.png')
screen.blit(pawn, (0, 0))
screen.fill(white)
screen.blit(pawn, (0,0))
pygame.display.flip()

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit()

sqr_size = 50 
notation_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
count = 0
notation = {}
for notation_letter in notation_letters:
    for notation_nr in range (1, 9):
        notation[str(notation_letter) + str(notation_nr)] = [sqr_size * count, sqr_size * (notation_nr -1)]
    count += 1

print(notation['a2'])