import numpy as np
import matplotlib.pyplot as plt

class Point:

    def __init__(self, x, y) :
        self.x, self.y = x, y
    
    def __str__(self) :
        return "Point(%.6F, %.6f) " % (self.x, self.y)
      
class Node:

    def contains(self, p) :
        """Does the node contain the point?"""
        raise NotImplementedError

class Primitive(Node) :
    
    def __init__(self, surface, sense) :
        self.surface, self.sense = surface, sense
        
    def contains(self, p) :
        return (self.surface.f(p) < 0) == self.sense

class Operator(Node):
    
    def __init__(self, L, R) :
        self.L, self.R = L, R
        ### ADD YOUR CODE HERE ###

    def contains(self, p) :
        raise NotImplementedError
      
class Union(Operator):
    
    def __init__(self, L, R) :
        super(Union, self).__init__(L, R)
        
    def contains(self, p) :
        inL = self.L.contains(p)
        inR = self.R.contains(p)
        return inL or inR
        
class Intersection(Operator):
    ### ADD YOUR CODE HERE ###
    pass 

class Surface:
    
    def f(self, p) :
        raise NotImplementedError
        
class QuadraticSurface(Surface):
    
    def __init__(self, A=0.0, B=0.0, C=0.0, D=0.0, E=0.0, F=0.0) :
        ### ADD YOUR CODE HERE ###
        pass
    
    def f(self, p) :
        ### ADD YOUR CODE HERE ###
        pass

class Circle(QuadraticSurface) :

    def __init__(self, r, x0=0, y0=0) :
        super(Circle, self).__init__(A=1, B=1, D=-2*x0, E=-2*y0, F=x0**2+y0**2-r**2)               
  
### ADD YOUR OTHER SURFACE CLASSES HERE ###

class Region(object) :
    
    def __init__(self) :
        self.node = None
    
    def append(self, node=None, surface=None, operation="U", sense=False) :
        assert((node and not surface) or (surface and not node))
        if isinstance(surface, Surface) :
            node = Primitive(surface, sense)
        if self.node is None :
            self.node = node
        else :
            O = Union if operation == "U" else Intersection
            self.node = O(self.node, node)
          
class Geometry(object) :
    
    # Attributes can be defined in the body of a class.  However, these
    # become "static" values that are the same for every object of the class.
    # Hence, they can be accessed either through object.attribute or 
    # classname.attribute.
    DEFAULT_REGION = -1    
    
    def __init__(self,  xmin, xmax, ymin, ymax) :
        self.xmin, self.xmax = xmin, xmax
        self.ymin, self.ymax = ymin, ymax
        self.regions = []
        
    def add_region(self, r) :
        self.regions.append(r)

    def find_region(self, p) :
        """ Find the region that contains the point.  If none 
        is found, return Geometry.noregion.
         
        Arguments:
            p : Point
        Returns:
            i : int
        """

        region = Geometry.DEFAULT_REGION
        ### YOUR CODE HERE ###
        return region
        
    def plot(self, nx, ny) :
        ### ADD YOUR CODE HERE ###
        pass
        
