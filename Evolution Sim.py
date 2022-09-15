import pygame,time
from random import *

pygame.init()

win=pygame.display.set_mode((900,900))
brown=(181,101,29)
win.fill(brown)
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
    def move(self):
        pass
    
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
    for x,y,z in zip(range(100),range(100),range(100)):
        pygame.draw.rect(win,(0,0,0),(x*9,1,1,899))
        pygame.display.update()
        pygame.draw.rect(win,(0,0,0),(1,y*9,899,1))
drawGrid()
pygame.display.update()
speciesList=[species(1,4,2,0,1,1,6,False,(210,180,140)),species(3,3,6,3,3,3,24,True,(255,128,0))]
animalList=[]
for i in range(25):
    x=speciesList[0].callFunction()
    animalList.append(animal(speciesList[0].callFunction(),randint(0,100),randint(0,100)))
    print(animalList[-1].x,animalList[-1].y)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
