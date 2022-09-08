import pygame,time

pygame.init()

win=pygame.display.set_mode((900,900))
brown=(58.8,129.4,0)
win.fill(brown)
pygame.display.update()

def drawGrid():
    
    for x,y,z in zip(range(100),range(100),range(100)):
        pygame.draw.rect(win,(0,0,0),(x*9,1,1,899))
        pygame.display.update()
        pygame.draw.rect(win,(0,0,0),(1,y*9,899,1))
    
drawGrid()
pygame.display.update()
while True:
    pass