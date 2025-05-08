import math
from copy import deepcopy

class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y
    
    def read(self):
        try:
            input_str = input()
            coords = input_str.split()
            if len(coords) >= 2:
                self.__x = int(coords[0])
                self.__y = int(coords[1])
            else:
                print("Lỗi: Vui lòng nhập hai số nguyên cách nhau bởi khoảng trắng")
        except ValueError:
            print("Lỗi: Vui lòng nhập hai số nguyên hợp lệ")
    
    def print(self):
        print(f"({self.__x}, {self.__y})")
    
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def distance(self, P=None):
        if P is None:
            # Khoảng cách đến gốc tọa độ (0,0)
            return math.sqrt(self.__x**2 + self.__y**2)
        else:
            # Khoảng cách đến điểm P
            return math.sqrt((P.getX() - self.__x)**2 + (P.getY() - self.__y)**2)

class LineSegment:
    def __init__(self, *args):
        if len(args) == 0:
            # Constructor mặc định
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)
        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
            # Constructor nhận 2 đối tượng Point
            self.__d1 = args[0]
            self.__d2 = args[1]
        elif len(args) == 4:
            # Constructor nhận 4 số nguyên x1, y1, x2, y2
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])
        elif len(args) == 1 and isinstance(args[0], LineSegment):
            # Constructor sao chép
            self.__d1 = Point(args[0].__d1.getX(), args[0].__d1.getY())
            self.__d2 = Point(args[0].__d2.getX(), args[0].__d2.getY())
    
    def read(self):
        try:
            input_str = input()
            coords = input_str.split()
            if len(coords) >= 4:
                x1, y1, x2, y2 = map(int, coords[:4])
                self.__d1 = Point(x1, y1)
                self.__d2 = Point(x2, y2)
            else:
                print("Lỗi: Vui lòng nhập bốn số nguyên cách nhau bởi khoảng trắng")
        except ValueError:
            print("Lỗi: Vui lòng nhập các số nguyên hợp lệ")
    
    def print(self):
        print(f"[({self.__d1.getX()}, {self.__d1.getY()}); ({self.__d2.getX()}, {self.__d2.getY()})]")
    
    def move(self, dx, dy):
        self.__d1.move(dx, dy)
        self.__d2.move(dx, dy)
    
    def length(self):
        return self.__d1.distance(self.__d2)
    
    def angle(self):
        dx = self.__d2.getX() - self.__d1.getX()
        dy = self.__d2.getY() - self.__d1.getY()
        
        # Tính góc bằng atan2 (đơn vị radian)
        angle_rad = math.atan2(dy, dx)
        
        # Chuyển đổi sang độ và chuẩn hóa về đoạn [0, 359]
        angle_deg = math.degrees(angle_rad)
        if angle_deg < 0:
            angle_deg += 360
            
        # Làm tròn đến số nguyên gần nhất
        return round(angle_deg)

class LineSegmentTest:
    @staticmethod
    def testCase1():
        print("Kịch bản 1:")
        A = Point(2, 5)
        B = Point(20, 35)
        AB = LineSegment(A, B)
        AB.move(35, 51)
        print("Đoạn thẳng AB sau khi tịnh tiến:")
        AB.print()
        print()
    
    @staticmethod
    def testCase2():
        print("Kịch bản 2:")
        CD = LineSegment()
        print("Nhập tọa độ của đoạn thẳng CD (x1 y1 x2 y2):")
        CD.read()
        print(f"|CD| = {CD.length():.2f}")
        print()
    
    @staticmethod
    def testCase3():
        print("Kịch bản 3:")
        print("Nhập số đoạn thẳng n:")
        n = int(input())
        segments = []
        
        print(f"Nhập {n} đoạn thẳng (mỗi đoạn gồm 4 số x1 y1 x2 y2):")
        for i in range(n):
            input_str = input()
            coords = list(map(int, input_str.split()))
            if len(coords) >= 4:
                segments.append(LineSegment(coords[0], coords[1], coords[2], coords[3]))
        
        # Sắp xếp đoạn thẳng theo chiều dài tăng dần
        segments.sort(key=lambda segment: segment.length())
        
        print("Danh sách đoạn thẳng theo thứ tự chiều dài tăng dần:")
        for segment in segments:
            segment.print()
    
    @staticmethod
    def main():
        LineSegmentTest.testCase1()
        LineSegmentTest.testCase2()
        LineSegmentTest.testCase3()

if __name__ == "__main__":
    LineSegmentTest.main() 