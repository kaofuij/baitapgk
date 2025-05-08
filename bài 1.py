import math

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

class PointTest:
    @staticmethod
    def main():
        # Tạo điểm A(3, 4) và hiển thị
        A = Point(3, 4)
        print("Tọa độ điểm A:", end=" ")
        A.print()
        
        # Tạo điểm B với giá trị nhập từ bàn phím và hiển thị
        print("Nhập tọa độ điểm B:", end=" ")
        B = Point()
        B.read()
        print("Tọa độ điểm B:", end=" ")
        B.print()
        
        # Tạo điểm C đối xứng với điểm B qua gốc tọa độ và hiển thị
        C = Point(-B.getX(), -B.getY())
        print("Tọa độ điểm C:", end=" ")
        C.print()
        
        # Hiển thị khoảng cách từ điểm B đến gốc tọa độ O
        print(f"Khoảng cách từ điểm B đến gốc tọa độ: {B.distance()}")
        
        # Hiển thị khoảng cách từ điểm A đến điểm B
        print(f"Khoảng cách từ điểm A đến điểm B: {A.distance(B)}")

if __name__ == "__main__":
    PointTest.main() 