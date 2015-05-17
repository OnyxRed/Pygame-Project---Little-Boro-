__version__="0.1"

import pygame,sys
from pygame.locals import*

pygame.init()

#We should probably begin with a generic class datatype, which I usually call 'object'

class Object(object):
    def __init__(self,pos,width,height):
        self.pos=pos
        self.width=width
        self.height=height

class Player(Object):
    def __init__(self,*arg,**kwargs):
        super(Player,self).__init__(*arg,**kwargs)

class Env(object):
    def __init__(self, bg,children):
        self.screen=pygame.display.set_mode((width,height))
        self.bg=bg
        self.children=children
        self.camera=camera
        self.width=width
        self.height=height
        self.clock=pygame.time.Clock()

    def run(self):
        self.draw()
        self.events()

    def draw(self):
        self.screen.blit(self.bg,pygame.Rect(0,0,width,height))

    def events(self):
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        pygame.display.update()
        self.clock.tick(50)

if __name__=="__main__":
    root=Env(bg=pygame.image.load("images/sky/sky.png"),children=[])
    
    
    
        

    


