__version__="0.01a"

import pygame,sys
from pygame.locals import*

pygame.init()

#We should probably begin with a generic class datatype, which I usually call 'object'

class Object(object): #Generic class objects
    def __init__(self,pos,width,height,image=None,color=None,state=None,*arg,**kwargs):
        self.pos=pos
        self.width=width
        self.height=height
        self.image=image
        self.color=color
        self.state=state

    def getRect(self):
        return pygame.Rect(self.pos,(self.width,self.height))

    def draw(self,screen):
        if self.image is not None:
            screen.blit(self.image[self.state[0]][self.state[1]],self.getRect())

        else:
            pygame.draw.rect(screen,self.color,self.getRect())

class Player(Object): #Player object
    def __init__(self,*arg,**kwargs):
        super(Player,self).__init__(*arg,**kwargs)
        
        

class Env(object): #Created basic environment
    def __init__(self, bg,children,width,height,camera=None):
        self.screen=pygame.display.set_mode((width,height))
        self.bg=pygame.transform.scale(bg,(width,height))
        self.children=children
        self.camera=camera
        self.width=width
        self.height=height
        self.clock=pygame.time.Clock()

    def run(self):
        while True:
            self.draw()
            self.events()
            self.update()

    def draw(self):
        self.screen.blit(self.bg,pygame.Rect(0,0,self.width,self.height))

        self.children["Player"].draw()

    def events(self):
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

            if even

    def update(self):
        pygame.display.update()
        self.clock.tick(50)
        
root=Env(bg=pygame.image.load("images/sky/sky.png"),children={"Player":Player(pos=(100,100),width=50,height=50,image={"Static":["images/boro/static.png"]},state=("Static",0)}],width=1000,height=600)
root.run()
    
    
        

    


