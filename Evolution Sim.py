import pygame,time,math
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
    def __init__(self,size,speed,maxhp,attack,defense,saturation,lifespan,breedingInterval,canEatMeat,colour=0):
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
        self.breedingInterval=breedingInterval
        self.killList=[]
        
    def updateKillList(self):
        self.killList=[]
        for i in speciesList:
            if i.size<=self.size and i!=self:
                self.killList.append(i)
    def callFunction(self):
        return self.size,self.speed,self.maxhp,self.attack,self.defense,self.saturation,self.lifespan,self.breedingInterval,self.canEatMeat,self,self.colour
class animal(object):
    def __init__(self,attributes,x=None,y=None):
        
        self.size=attributes[0]
        self.colour=attributes[10]
        self.speed=attributes[1]
        self.hp=attributes[2]
        self.maxhp=self.hp
        self.attack=attributes[3]
        self.defense=attributes[4]
        self.saturation=attributes[5]
        self.lifespan=attributes[6]
        self.canEatMeat=attributes[8]
        self.breedingInterval=attributes[7]
        self.x=x
        self.y=y
        self.species=attributes[9]
        self.age=0
        
    def draw(self):
        pygame.draw.rect(win,self.colour,(self.x*9+1,self.y*9+1,8,8))
    def move(self):
        if not self.wantBreed:
            if self.canEatMeat:
                target=animalList[0]
                targetDist=abs(self.x-animalList[0].x)+abs(self.y-animalList[0].y)
                for i in animalList:
                    if i.species in self.species.killList:
                        if abs(self.x-i.x+self.y-i.y)<targetDist:
                            target=i
                            targetDist=abs(self.x-i.x)+abs(self.y-i.y)
                tick=0
                for i in range(self.speed):
                    if tick==0 and self.x!=target.x or tick==1 and self.y==target.y:
                        if self.x<=target.x:
                            self.x+=1
                        elif self.x>=target.x:
                            self.x-=1
                        tick=1
                    elif tick==1 and self.y!=target.y or tick==0 and self.x==target.x:
                        if self.y<=target.y:
                            self.y+=1
                        elif self.y>=target.y:
                            self.y-=1
                        tick=0



            else:
                for i in range(self.speed):
                    x=randint(1,4)
                    if x==1:
                        if self.x+1>=90:
                            pass
                        else:
                            self.x+=1
                    elif x==2:
                        if self.x-1<0:
                            pass
                        else:
                            self.x-=1
                    elif x==3:
                        if self.y+1>=90:
                            pass
                        else:
                            self.y+=1
                    else:
                        if self.y-1<0:
                            pass
                        else:
                            self.y-=1
        else:
            target=animalList[0]
            targetDist=abs(self.x-animalList[0].x)+abs(self.y-animalList[0].y)
            for i in animalList:
                if i.species ==self.species:
                    if abs(self.x-i.x+self.y-i.y)<targetDist:
                        target=i
                        targetDist=abs(self.x-i.x)+abs(self.y-i.y)
            tick=0
            for i in range(self.speed):
                if tick==0 and self.x!=target.x or tick==1 and self.y==target.y:
                    if self.x<=target.x:
                        self.x+=1
                    elif self.x>=target.x:
                        self.x-=1
                    tick=1
                elif tick==1 and self.y!=target.y or tick==0 and self.x==target.x:
                    if self.y<=target.y:
                        self.y+=1
                    elif self.y>=target.y:
                        self.y-=1
                    tick=0
    def checkEat(self):
        if self.canEatMeat:
            for i in animalList:
                if i.species in self.species.killList:
                    if i.x==self.x and i.y==self.y:
                        self.eat(i)

    def eat(self,animal):
        animalList.remove(animal)
    
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
    def update(self):
        self.move()
        self.draw()
        self.checkEat()
        if self.sinceLastOffspring>=self.breedingInterval:
            self.wantBreed=True
            for i in animalList:
                if i.species==self.species and self.x==i.x and self.y==i.y:
                    self.breed(i)#
                    break
def drawGrid():
    win.fill(brown)
    for x,y in zip(range(100),range(100)):
        pygame.draw.rect(win,(0,0,0),(x*9,1,1,899))
        pygame.draw.rect(win,(0,0,0),(1,y*9,899,1))
drawGrid()
pygame.display.update()
#size,speed,maxhp,attack,defense,saturation,lifespan,breedingInterval,canEatMeat,colour=0
speciesList=[species(1,4,2,0,1,1,0,6,False,(210,180,140)),species(3,3,6,3,3,3,0,24,True,(255,128,0))]
for i in speciesList:
    if i.canEatMeat:
        i.updateKillList()
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
        i.update()
    pygame.display.update()
while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]and fps<120:
        fps+=5
    elif keys[pygame.K_DOWN] and fps>5:
        fps-=5
    update()
