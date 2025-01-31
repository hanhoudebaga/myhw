import unittest
import math

def classify_triangle(a, b, c):
    if not all(isinstance(side, (int, float)) for side in (a, b, c)):
        return "Invalid input: all inputs must be numbers"
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid input: all inputs must be positive"
    if (a + b <= c) or (b + c <= a) or (a + c <= b):
        return "Invalid triangle"
    if a == b == c:
        type = "Equilateral triangle"
    elif a == b or b == c or a == c:
        type = "Isosceles triangle"
    else:
        type = "Scalene triangle"
        
    if (math.isclose(a ** 2 + b ** 2, c ** 2) or 
        math.isclose(a ** 2 + c ** 2, b ** 2) or 
        math.isclose(b ** 2 + c ** 2, a ** 2)):
        type += " and right triangle"
        
    return type

class TestTriangleClassification(unittest.TestCase):
  def test_invalid_triangles(self):
    self.assertEqual(classify_triangle(-3, 4, 5), "Invalid input: all inputs must be positive");
    self.assertEqual(classify_triangle('3', 4, 5), "Invalid input: all inputs must be numbers");
  
  def test_triangles(self):
    self.assertEqual(classify_triangle(3, 3, 3), "Equilateral triangle");
    self.assertEqual(classify_triangle(3, 3, 5), "Isosceles triangle");
    self.assertEqual(classify_triangle(4, 5, 6), "Scalene triangle");
    self.assertEqual(classify_triangle(3, 4, 5), "Scalene triangle and right triangle");
    self.assertEqual(classify_triangle(1, 1, math.sqrt(2)), "Isosceles triangle and right triangle")
       
if __name__ == '__main__':
    unittest.main()
