import math
class Circle:
  def __init__(self, radius):
    self.__radius = radius # 주의! 이렇게 되면 외부에서 사용할 수 없는 변수가 됨!
  def get_circumstance(self):
    return 2 * 3.14 * self.__radius
  def get_area(self):
    return 3.14 * (self.__radius ** 2)
  
circle = Circle(10)
print("# 원의 둘레와 넓이를 구합니다.")
print("원의 둘레:", circle.get_circumstance())
print("원의 둘레:", circle.get_area())
print()
print("# __radius 에 접근합니다.")
print(circle.__radius)