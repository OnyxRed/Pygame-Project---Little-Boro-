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

def generatePlatforms(children):
    myList=[]
    
    for x in children:
        if x!="Player":
            for y in range(len(children[x])):
                if children[x][y].Class=="platform":
                    myList.append((pygame.Rect(children[x][y].pos,(children[x][y].width,children[x][y].height)),(x,y)))

    return myList

class Object(object): #Generic class objects
    def __init__(self,pos,width,height,image=None,color=None,state=None,*arg,**kwargs):
        self.pos=pos
        self.width=width
        self.height=height
        self.image=image
        self.color=color
        self.state=state
        self.Class="obj"

    def getRect(self):
        return pygame.Rect(self.pos,(self.width,self.height))

    def draw(self,screen):
        if self.image is not None:
            screen.blit(self.image[self.state[0]][self.state[1]],self.getRect())

        else:
            pygame.draw.rect(screen,self.color,self.getRect())

class Platform(Object):
    def __init__(self,collidable=None,*arg,**kwargs):
        self.collidable=collidable
        super(Platform,self).__init__(*arg,**kwargs)
        self.Class="platform"
                            
class Player(Object): #Player object
    def __init__(self,*arg,**kwargs):
        super(Player,self).__init__(*arg,**kwargs)
        self.Class="player"
        self.root=False
        self.vector=(0,0)
        self.speed=3
        self.jump=10

    def update(self,master):
        if not self.root:
            self.vector=addTuples(self.vector,(0,master.gravity))
            if self.vector[1]>10:
                self.vector=assignTuple(self.vector,10,1)

        myList=generatePlatforms(master.children)

        myRect=self.getRect()

        for x in range(len(myList)):
            if myRect.colliderect(myList[x][0]):
                if master.children[myList[x][1][0]][myList[x][1][1]].collidable is None:
                    if self.pos[1]>master.children[myList[x][1][0]][myList[x][1][1]][1]:
                        self.root=None
                        self.vector=(0,0)
                        
                self.root=master.children[myList[x][1][0]][myList[x][1][1]]
                self.vector=assignTuple(self.vector,0,1)
                break

            if x==len(myList)-1:
                self.root=False

        self.pos=addTuples(self.pos,self.vector)
            
class Env(object): #Created basic environment
    def __init__(self, bg,children,width,height,camera=None):
        self.screen=pygame.display.set_mode((width,height))
        self.bg=pygame.transform.scale(bg,(width,height))
        self.children=children
        self.camera=camera
        self.width=width
        self.height=height
        self.clock=pygame.time.Clock()
        self.gravity=1

    def run(self):
        while True:
            self.draw()
            self.events()
            self.update()

    def draw(self):
        self.screen.blit(self.bg,pygame.Rect(0,0,self.width,self.height))

        self.children["Player"].draw(self.screen)

        for x in self.children:
            if x!="Player":
                for y in range(len(self.children[x])):
                    self.children[x][y].draw(self.screen)

    def events(self):
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

            if event.type==KEYDOWN:
                if event.key==K_LEFT:
                    self.children["Player"].vector=(-self.children["Player"].speed,0)

                if event.key==K_RIGHT:
                    self.children["Player"].vector=(self.children["Player"].speed,0)

                if event.key==K_UP:
                    if self.children["Player"].root is None:
                        self.children["Player"].vector=(0,-self.children["Player"].jump)

            if event.type==KEYUP:
                self.children["Player"].vector=(0,0)
                    
    def update(self):
        self.children["Player"].update(self)
        
        pygame.display.update()
        self.clock.tick(50)
        
root=Env(bg=pygame.image.load("C:/Users/MrCarrot/Pictures/city.jpg"),children={"Player":Player(pos=(100,100),color=(255,0,0),width=50,height=50),
                                                                               "Platforms":[Platform(pos=(100,300),color=(0,255,0),width=100,height=10,collidable=False)]},width=1000,height=600)
root.run()

#image = image={"Static":["images/boro/static.png"]
#state = ,state=("Static",0)
        

    


