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

def filterChildren():
    global level
    global player
    global root

    for x in level.children:
        if player.centerx() in range(x[0][0],x[0][1]):
            if player.bottom() in range(x[1][0],x[1][1]):
                root=x
                return True

    root=None

    return False

WIDTH=1000
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Little boro")

clock=pygame.time.Clock()

class Object(object):
    def __init__(self,pos,width,height,image=None,color=None,bounce=None):
        self.pos=pos
        self.width=width
        self.height=height
        self.rect=lambda:pygame.Rect(self.pos,(self.width,self.height))
        self.bottom=lambda:self.pos[1]+self.height
        self.centerx=lambda:self.pos[0]+self.width/2
        self.bounce=bounce

        if image is not None:
            self.image=pygame.transform.scale(image,(self.width,self.height))

        else:
            self.image=None
            
        self.color=color

    def draw(self):
        global screen
        
        if self.image is not None:
            screen.blit(self.image,self.rect())

        else:
            pygame.draw.rect(screen,self.color,self.rect())

    def act(self):
        global vector
        global screen
        
        if self.bounce is not None:
            if self.rect().colliderect(player.rect()):
                vector=addTuples(vector,(0,-self.bounce))
            

class Env(object):
    def __init__(self,bg,children):
        global WIDTH,HEIGHT
        
        self.bg=pygame.transform.scale(bg,(WIDTH,HEIGHT))
        self.children=children
        self.rect=pygame.Rect((0,0),(WIDTH,HEIGHT))
        self.gravity=2

    def draw(self):
        global screen

        screen.blit(self.bg,self.rect)

class Platform(Object):
    def __init__(self,*arg,**kwargs):
        super(Platform,self).__init__(*arg,**kwargs)


player=Object(pos=(100,100),width=50,height=50,image=pygame.image.load("images/sprites/sprite_chav.png"))
level=Env(bg=pygame.image.load("C:/Users/MrCarrot/Pictures/city.jpg"),children={
    ((100,200),(300,340)):Platform(pos=(100,300),width=100,height=30,color=(0,0,0)),
    ((300,400),(200,240)): Platform(pos=(300,200),width=100,height=100,color=(255,0,0)),
    ((600,800),(500,540)):Platform(pos=(600,500),width=200,height=10,color=(0,255,0),bounce=100)})

vector=(0,0)

speed=0.5

root=None

pressed=0

jump=30

static=False

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            terminate()

        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                pressed=1

            if event.key==K_RIGHT:
                pressed=2

            if root is not None:
                if event.key==K_SPACE:
                    vector=addTuples(vector,(0,-jump))
                
        if event.type==KEYUP:
            pressed=0
            if root is not None:
                vector=assignTuple(vector,0,0)

            else:
                vector=assignTuple(vector,vector[0]/2,0)

    level.draw()
    player.draw()

    for x in level.children:
        level.children[x].draw()
        level.children[x].act()

    if pressed==1:
        root=None
        vector=addTuples(vector,(-speed,0))

    if pressed==2:
        root=None
        vector=addTuples(vector,(speed,0))

    player.pos=(round(player.pos[0]),round(player.pos[1]))

    if filterChildren():
        if not static:
            vector=(0,0)
            static=True

    else:
        vector=addTuples(vector,(0,level.gravity))

    if root is None:
        static=False

    else:
        player.pos=assignTuple(player.pos,root[1][0]-player.height+1,1)
        
    player.pos=addTuples(player.pos,vector)

    pygame.display.update()
    clock.tick(50)
    


