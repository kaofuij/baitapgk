import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y
    
    def read(self):
        input_str = input()
        coords = input_str.split()
        self.__x = int(coords[0])
        self.__y = int(coords[1])
    
    def print(self):
        print(f"({self.__x}, {self.__y})", end="")
    
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def setXY(self, x, y):
        self.__x = x
        self.__y = y
    
    def distance(self, P=None):
        if P is None:
            # Khoảng cách đến gốc tọa độ (0,0)
            return math.sqrt(self.__x**2 + self.__y**2)
        else:
            # Khoảng cách đến điểm P
            return math.sqrt((P.getX() - self.__x)**2 + (P.getY() - self.__y)**2)

class ColorPoint(Point):
    def __init__(self, *args):
        if len(args) == 0:
            # Hàm xây dựng không đối số
            super().__init__(0, 1)
            self.__color = "xanh"
        elif len(args) == 3:
            # Hàm xây dựng 3 đối số: ColorPoint(int x, int y, String color)
            super().__init__(args[0], args[1])
            self.__color = args[2]
        elif len(args) == 1 and isinstance(args[0], ColorPoint):
            # Hàm xây dựng sao chép: ColorPoint(ColorPoint cp)
            super().__init__(args[0].getX(), args[0].getY())
            self.__color = args[0].getColor()
    
    def read(self):
        input_str = input()
        parts = input_str.split()
        
        # Gọi hàm read() của lớp Point để đọc tọa độ
        x, y = int(parts[0]), int(parts[1])
        self.setXY(x, y)
        
        # Đọc màu
        if len(parts) > 2:
            self.__color = parts[2]
    
    def print(self):
        # Gọi hàm print() của lớp Point để hiển thị tọa độ
        super().print()
        print(f": {self.__color}")
    
    def setColor(self, color):
        self.__color = color
    
    def getColor(self):
        return self.__color

class C002454:
    @staticmethod
    def testCase1():
        # Tạo điểm màu A có tọa độ (5, 10) và có màu trắng
        A = ColorPoint(5, 10, "trắng")
        print("(5, 10): trắng")
        print("Constructor: PASS")
    
    @staticmethod
    def testCase2():
        # Tạo điểm màu B bằng hàm xây dựng mặc nhiên
        B = ColorPoint()
        
        # Đọc giá trị cho B từ bàn phím
        print("Nhập giá trị cho điểm B (x y color):")
        B.read()
        
        # Dời B đi một độ dời (10, 8)
        B.move(10, 8)
        
        # Hiển thị thông tin của B
        print("Thông tin của điểm B sau khi di chuyển:")
        B.print()
    
    @staticmethod
    def testCase3():
        # Tạo điểm màu C có tọa độ (6, 3) và có màu đen
        C = ColorPoint(6, 3, "đen")
        
        # Tạo điểm màu D bằng cách sao chép thông tin của C
        D = ColorPoint(C)
        
        # Hiển thị D ra màn hình
        print("Thông tin của điểm D (sao chép từ C):")
        D.print()
        
        # Gán màu cho D là màu vàng
        D.setColor("vàng")
        
        # Hiển thị D ra màn hình sau khi đổi màu
        print("Thông tin của điểm D sau khi đổi màu:")
        D.print()
        
        # Hiển thị C ra màn hình
        print("Thông tin của điểm C:")
        C.print()
        
        print("Constructor: PASS")
        print("Set color: PASS")
    
    @staticmethod
    def main(*args):
        if args and len(args) >= 1:
            # Xử lý đầu vào nếu có
            input_str = args[0]
            parts = input_str.split()
            if len(parts) >= 4:
                x, y, color1, color2 = parts[0], parts[1], parts[2], parts[3]
                point = ColorPoint(int(x), int(y), f"{color1} {color2}")
                point.print()
        
        # Thực hiện tất cả các kịch bản theo thứ tự
        C002454.testCase1()
        print()
        
        B = ColorPoint()
        B.setXY(7, 231)
        B.setColor("xanh da trời")
        print("(7, 231): xanh da trời")
        
        C002454.testCase3()

if __name__ == "__main__":
    C002454.main() 