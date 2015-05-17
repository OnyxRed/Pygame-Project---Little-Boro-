__version__="0.1"

#We should probably begin with a generic class datatype, which I usually call 'object'

class Object(object):
    def __init__(self,pos,width,height):
        self.pos=pos
        self.width=width
        self.height=height

