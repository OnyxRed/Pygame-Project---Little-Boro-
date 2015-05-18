__version__="0.01a"

import pygame,sys
from pygame.locals import*

pygame.init()

#We should probably begin with a generic class datatype, which I usually call 'object'

def addTuples(tuple1,tuple2): #No need to use numpy!
    tuple3=[]

    for x in range(len(tuple1)):
        tuple3.append(tuple1[x]+tuple2[x])

    return tuple(tuple3)

def assignTuple(Tuple,val,index):
    tuple2=list(Tuple)

    tuple2[index]=val

    return tuple(tuple2)

def terminate():
    pygame.quit()
    sys.exit()

WIDTH=1000
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Little boro")

clock=pygame.time.Clock()

class Object(object):
    def __init__(self,pos,width,height,image=None,color=None):
        self.pos=pos
        self.width=width
        self.height=height
        self.rect=lambda:pygame.Rect(self.pos,(self.width,self.height))
        self.image=pygame.transform.scale(image,(self.width,self.height))
        self.color=color

    def draw(self):
        global screen

        if self.image is not None:
            screen.blit(self.image,self.rect())

        else:
            pygame.draw.rect(screen,self.color,self.rect())

class Env(object):
    def __init__(self,bg,children):
        global WIDTH,HEIGHT
        
        self.bg=pygame.transform.scale(bg,(WIDTH,HEIGHT))
        self.children=children
        self.rect=pygame.Rect((0,0),(WIDTH,HEIGHT))

    def draw(self):
        global screen

        screen.blit(self.bg,self.rect)


player=Object(pos=(100,100),width=50,height=50,image=pygame.image.load("images/sprites/sprite_chav.png"))
level=Env(bg=pygame.image.load("C:/Users/MrCarrot/Pictures/city.jpg"),children=[])

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            terminate()

    player.draw()
    level.draw()

    pygame.display.update()
    clock.tick(50)
    


