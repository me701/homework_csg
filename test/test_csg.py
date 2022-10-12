"""
This file is an example of a *unit-test suite*.  It is good practice to 
develop such a suite for a Python module.  The unittest module makes
this much easier, but it is not the only way.  In reality, a set of 
tests that *covers* all of the functions/methods of one's code is
the best way to avoid bugs (in the present and in the future).

"""

import csg
import unittest
import numpy as np

class TestCSG(unittest.TestCase) :

    def setUp(self) :
        pass

    #-------------------------------------------------------------------------#
    # TESTS OF POINT CLASS
    #-------------------------------------------------------------------------#

    def testPoint_translate(self) :        
        p0 = csg.Point(1.0, 2.0)
        p1 = p0 + csg.Point(2.0, 3.0)
        self.assertEqual(p1.x, 3.0)
        self.assertEqual(p1.y, 5.0)
    
    def testPoint_scale(self) :
        p0 = csg.Point(1.0, 2.0)
        p1 = p0 * 2.0
        self.assertEqual(p1.x, 2.0)
        self.assertEqual(p1.y, 4.0) 
        
    #-------------------------------------------------------------------------#
    # TESTS OF SURFACE CLASSES
    #-------------------------------------------------------------------------#
    
    def testQuadraticSurface_f_plane(self) :
        
        # vertical plane at x = 3
        v = csg.QuadraticSurface(D=1, F=-3)
        self.assertAlmostEqual(v.f(csg.Point(1, 0)), -2)
        
        # create a circle of radius 2 centered at (2, 2)      
        c = csg.QuadraticSurface(A=1, B=1, D=-4, E=-4, F=4)
        self.assertAlmostEqual(c.f(csg.Point(0, 2)), 0.0)
        
    def testPlaneV(self) :
        v = csg.PlaneV(3)
        self.assertEqual(v.D, 1)
        self.assertEqual(v.F, -3)
        
    def testPlaneH(self) :
        v = csg.PlaneH(3)
        self.assertEqual(v.E, 1)
        self.assertEqual(v.F, -3)        

    def testPlane(self) :
        v = csg.Plane(1, 1)
        self.assertEqual(v.D, -1)
        self.assertEqual(v.E, 1)
        self.assertEqual(v.F, -1)
        
    def testCircle(self) :
        c = csg.Circle(1, 1, 1)
        self.assertEqual(c.A, 1)
        self.assertEqual(c.B, 1)
        self.assertEqual(c.D, -2)
        self.assertEqual(c.E, -2)
        self.assertEqual(c.F, 1)

    #-------------------------------------------------------------------------#
    # TESTS OF NODE CLASSES
    #-------------------------------------------------------------------------#
      
    def testPrimitive(self) :

        # unit circle centered at origin        
        c = csg.Circle(1, 0, 0)
        
        # create node that represents the inside of the circle.  the 
        # "sense" argument specifies whether the node should represent
        # everything inside (true) or outside (false) of the surface.
        inside_c = csg.Primitive(c, sense=True)
        self.assertTrue(inside_c.contains(csg.Point(0, 0)))
        self.assertFalse(inside_c.contains(csg.Point(2, 2)))
    
        outside_c = csg.Primitive(c, sense=False)
        self.assertFalse(outside_c.contains(csg.Point(0, 0)))
        self.assertTrue(outside_c.contains(csg.Point(2, 2)))
        
    def get_circles(self) :
        # unit circle centered at origin
        c0 = csg.Circle(1)
        # circle of radius two centered at the origin
        c1 = csg.Circle(2)
        return c0, c1
        
    def testUnion_surface(self) :
        c0, c1 = self.get_circles()
        self.assertTrue(c0.f(csg.Point(1.5, 0)) > 0.0)
        self.assertTrue(c1.f(csg.Point(1.5, 0)) > 0.0)
        
    def testUnion_contains(self) :
        c0, c1 = self.get_circles()
        l, r = csg.Primitive(c0, True), csg.Primitive(c1, False)
        # everything outside c1 and inside c0
        u = csg.Union(l, r)
        self.assertTrue(u.contains(csg.Point(0, 0)))
        self.assertTrue(u.contains(csg.Point(2, 0)))
        self.assertFalse(u.contains(csg.Point(1.5, 0)))

    def testIntersection_contains(self) :
        
        c0, c1 = self.get_circles()
        l, r = Primitive(c0, False), csg.Primitive(c1, True)
        # everything between c0 and c1
        i = csg.Intersection(l, r)
        self.assertFalse(i.contains(csg.Point(0, 0)))
        self.assertFalse(i.contains(csg.Point(2, 0)))
        self.assertTrue(i.contains(csg.Point(1.5, 0)))
        
    #-------------------------------------------------------------------------#
    # TESTS OF REGION CLASS
    #-------------------------------------------------------------------------#
      
    def get_region(self) :
        c0, c1 = self.get_circles()
        # produce a region that represents the area between the two circles
        region = csg.Region()
        region.append(surface=c0, sense=False, operation="I")
        region.append(surface=c1, sense=True, operation="I")
        return region

    def get_region_2(self) :
        L = csg.PlaneV(0)
        R = csg.PlaneV(1)
        B = csg.PlaneH(0)
        T = csg.PlaneH(1)
        region = csg.Region()
        region.append(surface=L, sense=False)
        region.append(surface=R, sense=True, operation="I")
        region.append(surface=B, sense=False, operation="I")
        region.append(surface=T, sense=True, operation="I")
        return region
        
    def testRegion_contains(self) :
        
        region = self.get_region()
        self.assertFalse(region.node.contains(csg.Point(0, 0)))
        self.assertFalse(region.node.contains(csg.Point(2, 0)))
        self.assertTrue(region.node.contains(csg.Point(1.5, 0)))
  
        region = self.get_region_2()
        print(region.node.contains(csg.Point(0.5, 0.5)))
        
if __name__ == '__main__' :
    unittest.main()    
    
