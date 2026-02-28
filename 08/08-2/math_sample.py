import math
class Circle:
  def __init__(self, radius):
    self.radius = radius
  def get_circumstance(self):
    return 2 * 3.14 * self.radius
  def get_area(self):
    return 3.14 * (self.radius ** 2)
  
circle = Circle(10)
print("원의 둘레:", circle.get_circumstance())
print("원의 둘레:", circle.get_area())