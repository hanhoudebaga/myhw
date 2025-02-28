"""Classify the triangles"""
import unittest
import math

def classify_triangle(a, b, c):
    """Classify the triangles"""
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
    """Test Class"""
    def test_negative_input(self):
        """Test Negative Input"""
        self.assertEqual(classify_triangle(-3, 4, 5), "Invalid input: all inputs must be positive")
    def test_non_numeric_input(self):
        """Test Non Numeric Input"""
        self.assertEqual(classify_triangle('3', 4, 5), "Invalid input: all inputs must be numbers")
    def test_equilateral(self):
        """Test Equilateral"""
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral triangle")
    def test_isosceles(self):
        """Test Isosceles"""
        self.assertEqual(classify_triangle(3, 3, 5), "Isosceles triangle")
    def test_scalene_non_right(self):
        """Test Scalene Non Right"""
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene triangle")
    def test_scalene_right(self):
        """Test Scalene Right"""
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene triangle and right triangle")
    def test_isosceles_right(self):
        """Test Isosceles Right"""
        self.assertEqual(classify_triangle(1, 1, math.sqrt(2)),
        "Isosceles triangle and right triangle")
if __name__ == '__main__':
    unittest.main()
