import pygame,time
from random import *

pygame.init()

win=pygame.display.set_mode((900,900))
brown=(181,101,29)
pygame.display.update()

def getColour():
    colour=(randint(0,255),randint(0,255),randint(0,255))
    for i in speciesList:
        if i.colour==colour:
            getColour()
    return colour
class species():
    def __init__(self,size,speed,maxhp,attack,defense,saturation,lifespan,canEatMeat,colour=0):
        if colour==0:
            self.colour=getColour()
        else:
            self.colour=colour
        self.size=size
        self.speed=speed
        self.hp=maxhp
        self.maxhp=self.hp
        self.attack=attack
        self.defense=defense
        self.saturation=saturation
        self.lifespan=lifespan
        self.canEatMeat=canEatMeat
    
    def callFunction(self):
        return self.size,self.speed,self.maxhp,self.attack,self.defense,self.saturation,self.lifespan,self.canEatMeat,self,self.colour
class animal(object):
    def __init__(self,attributes,x=None,y=None):
        
        self.size=attributes[0]
        self.colour=attributes[9]
        self.speed=attributes[1]
        self.hp=attributes[2]
        self.maxhp=self.hp
        self.attack=attributes[3]
        self.defense=attributes[4]
        self.saturation=attributes[5]
        self.lifespan=attributes[6]
        self.canEatMeat=attributes[7]
        self.x=x
        self.y=y
        self.species=attributes[8]
        self.age=0
    
    def draw(self):
        pygame.draw.rect(win,self.colour,(self.x*9+1,self.y*9+1,8,8))
    def move(self):
        for i in range(self.speed):
            x=randint(1,4)
            if x==1:
                self.x+=1
            elif x==2:
                self.x-=1
            elif x==3:
                self.y+=1
            else:
                self.y-=1
    def eat(self):
        pass
    
    def attack(self,defender):
        pass
    
    def defend(self,attacker):
        pass
    
    def breed():
        pass
    
    def die():
        pass
    
    def checkIfDie(self):
        pass

def drawGrid():
    win.fill(brown)
    for x,y in zip(range(100),range(100)):
        pygame.draw.rect(win,(0,0,0),(x*9,1,1,899))
        pygame.draw.rect(win,(0,0,0),(1,y*9,899,1))
drawGrid()
pygame.display.update()
speciesList=[species(1,4,2,0,1,1,6,False,(210,180,140)),species(3,3,6,3,3,3,24,True,(255,128,0))]
animalList=[]
clock=pygame.time.Clock()
fps=5
for i in range(25):
    animalList.append(animal(speciesList[0].callFunction(),randint(0,100),randint(0,100)))
for i in range(4):
    animalList.append(animal(speciesList[1].callFunction(),randint(0,100),randint(0,100)))
def update():
    drawGrid()
    for i in animalList:
        i.move()
        i.draw()
    pygame.display.update()
while True:
    clock.tick(fps)
    deltatime=clock.tick(60)/1024
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    update()
