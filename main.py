__version__="0.01a"

import pygame,sys
from pygame.locals import*

pygame.init()

#We should probably begin with a generic class datatype, which I usually call 'object'

class Object(object): #Generic class objects
    def __init__(self,pos,width,height,*arg,**kwargs):
        self.pos=pos
        self.width=width
        self.height=height

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

    def events(self):
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        pygame.display.update()
        self.clock.tick(50)
        
root=Env(bg=pygame.image.load("images/sky/sky.png"),children=[Player(pos=(100,100),width=50,height=50)],width=1000,height=600)
root.run()
    
    
        

    


