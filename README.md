# Homework - Constructive-Solid Geometry

This homework focuses on the development of a
simple 2-D constructive solid geometry module.  I have provided you
with templates for many of classes you need to define.  The following
problems provide software specifications for pieces of your 
module, starting from points, and building on up through a 
whole geometry made of regions.

To help you in your development,
I've also provide a small unit test framework.  You should read
the unit test lesson on the Python from Scratch site for more.
The various unit tests demonstrate how your classes and methods
should work for a few cases.  The tests I provide may not provide
complete *coverage*, i.e., they might not test every method
for every possible use consistent with the specifications below.
You should feel free to modify these tests and add your own.  
Such testing is extremely helpful for all but the smallest programming
tasks, as it (1) formalizes the normal testing you would do in a (probably) much
sloppier way and (2) lives on as a set of (hopefully) easily understood
examples for how your code works.  Invaluable for the coder with 
the memory of a (dying) goldfish.

## Problem 1 

We started off our discussion of object-oriented programming
using the `Point`class as an example.  In essence, a 
`Point`represents a point in 2-D space (or, equivalently,
a 2-D vector starting from the origin).  In some applications,
it would be helpful to add two points (a translation), or to 
multiply a point by some constant (a scaling), e.g.,

```
>>> p1 = Point(1, 2)
>>> p2 = Point(2, 3)
>>> p3 = p1 + p3
>>> print(p3)
Point(x=3.000000, y=5.000000)
>>> p4 = p1 * 2
>>> print(p4)
Point(x=2.000000, y=4.000000)
```

**Deliverables**: Modify the basic `Point`class to handle addition of
two points and scaling of a point by a scalar value.



## Problem 2 

The template code provides partial definitions for 
the abstract `Surface`and concrete 
`QuadraticSurface`classes.  Your
first task is to implement the `f`method of `QuadraticSurface`.\\

Although you can define any 2-D quadratic surface with the approach
outlined in the notes, it is easier to specialize that
class further for common cases.  Your job is to 
create the following classes that inherit from `QuadraticSurface`:

  - `class PlaneV`; defines a vertical plane at $x=a$ via `v = PlaneV(a)`,
  - `class PlaneH`; defines a horizontal plane at $y=b$ via
        `h = PlaneH(b)`
  - `class Plane` defines a plane of the form $y = mx + b$
        via `p = Plane(m, b)`.
  - `class Circle`; defines a circle of radius $r$ and center $(a, b)$
       via `c = Circle(r, a, b)`.

**Deliverables**:

  1.  Implement `QuadraticSurface.f(p)`
  2. Implement `PlaneV`
  3. Implement `PlaneH`
  4. Implement `Plane`
  5. Implement `Circle`



## Problem 3


The template code includes definitions for 
an abstract `Node`class, from which 
the  `Primitive`and  `Operator`classes 
are derived.  An *abstract& class 
is one that defines a method signature but 
does not provide an implementation.  
A *concrete* class inherits
from a *base* class and provides an 
implementation of the methods. 

The `Primitive`class is a concrete class 
that represents
terminal node, i.e., a single surface.  On the other hand,
the  `Operator`class represents a generic combination
of two nodes.  Like `Node`, 
`Operator`is an abstract
class because its `contains` method is 
not (and should not) be implemented. 

In addition,  you  should create the following two specializations
of the `Operator`class:

  - `class Union`, whose method `contains(p)`
     should return `True` if the point is in either 
     its left or right nodes and `False`otherwise.
  - `class Intersection`, whose `contains(p)`
    should return `True` if the point is in both 
    its left and right nodes and `False` otherwise.

**Deliverables**:

  1. Implement `Operator.intersections(r)`
  2. Define `Union`and implement `Union.contains(p)`
  3. Define `Intersection`and implement `Intersection.contains(p)`



## Problem 4 

Now you have surfaces and nodes with which to 
implement a `Region` class.  I've proposed the 
following definition:

```python
class Region:
    
    def __init__(self) :
        self.node = None

    def append(self, node=None, surface=None, operation="U", sense=False) :
        assert((node and not surface) or (surface and not node))
        assert(operation in ["U", "I"])
        if isinstance(surface, Surface) :
            node = Primitive(surface, sense)
        if self.node is None :
            self.node = node
        else :
            O = Union if operation == "U" else Intersection
            self.node = O(self.node, node)

    def contains(self, p) :
        pass 
```

Study the `append` method because it represents
how we put all the surfaces and nodes together.  The 
key point is that `Region` has an attribute 
`node` that represents at all times the top of 
the tree of nodes and surfaces.  You should add 
an appropriate `docstring` to explain what the method
is doing, what the assertions are doing, etc.  In 
other words, make it obvious that you know what
*I'm* doing.  (This might seem like a silly exercise,
but the ability to digest and then add to code
that someone else wrote is a good way to improve
your own programming.) 

## Problem 5

Finally, consider the following {\tt Geometry} class:

```python
class Geometry(object) :
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
        pass

    def plot(self, xmin, xmax, nx, ymin, ymax, ny) :
        pass
```

Its construction requires a bounding box defined 
by minimum and maximum values for $x$ and $y$, i.e.,
the square domain in which the geometry is confined.
Regions are stored in an initially empty list.  Regions
are added by the `add_region` method.  Your job
is to implement the `find_region` method, which 
returns the index (in the list) of the region that
contains the point.  If no region contains the point,
or if the point lives outside the bounding box, return
`Geometry.DEFAULT_REGION`. 
