import json
import math
from collections import Counter
import os

class TuLanh:
    def __init__(self, other=None):
        if other is None:
            # Mặc định
            self.__nhanhieu = "Elextrolux"
            self.__maso = "UNKNOWN"
            self.__nuocsx = "Việt Nam"
            self.__tkdien = True
            self.__dungtich = 256
            self.__gia = 7000000
        elif isinstance(other, TuLanh):
            # Sao chép
            self.__nhanhieu = other.__nhanhieu
            self.__maso = other.__maso
            self.__nuocsx = other.__nuocsx
            self.__tkdien = other.__tkdien
            self.__dungtich = other.__dungtich
            self.__gia = other.__gia
        elif isinstance(other, list):
            # Truyền tham số (nhanhieu, maso, nuocsx, tkdien, dungtich, gia)
            self.__nhanhieu = other[0] if len(other) > 0 else "Elextrolux"
            self.__maso = other[1] if len(other) > 1 else "UNKNOWN"
            self.__nuocsx = other[2] if len(other) > 2 else "Việt Nam"
            self.__tkdien = other[3] if len(other) > 3 else True
            self.__dungtich = other[4] if len(other) > 4 else 256
            self.__gia = other[5] if len(other) > 5 else 7000000
    
    # Sao chép từ đối tượng khác
    def makeCopy(self, tl):
        self.__nhanhieu = tl.__nhanhieu
        self.__maso = tl.__maso
        self.__nuocsx = tl.__nuocsx
        self.__tkdien = tl.__tkdien
        self.__dungtich = tl.__dungtich
        self.__gia = tl.__gia
    
    def nhapThongTin(self):
        self.__nhanhieu = input()
        self.__maso = input()
        self.__nuocsx = input()
        self.__tkdien = input().lower() == "true"
        self.__dungtich = int(input())
        self.__gia = int(input())
    
    def hienThi(self):
        print("========")
        print(f"Nhãn hiệu: {self.__nhanhieu}")
        print(f"Mã số: {self.__maso}")
        print(f"Nước SX: {self.__nuocsx}")
        print(f"T/K điện: {'Có' if self.__tkdien else 'Không'}")
        print(f"Dung tích: {self.__dungtich}L")
        print(f"Giá: {self.__gia}VND")
        print("========")
    
    def layNhanHieu(self):
        return self.__nhanhieu
    
    def layGia(self):
        return self.__gia
    
    def soNguoiSD(self):
        return math.floor(self.__dungtich / 100)
    
    def cungNhanHieu(self, tl):
        return self.__nhanhieu == tl.__nhanhieu
    
    def nhHon(self, tl):
        return self.__dungtich < tl.__dungtich
    
    # Phương thức cho phép chuyển đối tượng thành dictionary để serialize
    def to_dict(self):
        return {
            "nhanhieu": self.__nhanhieu,
            "maso": self.__maso,
            "nuocsx": self.__nuocsx,
            "tkdien": self.__tkdien,
            "dungtich": self.__dungtich,
            "gia": self.__gia
        }
    
    # Phương thức từ dictionary đến đối tượng để deserialize
    @classmethod
    def from_dict(cls, data):
        tl = cls()
        tl.__nhanhieu = data["nhanhieu"]
        tl.__maso = data["maso"]
        tl.__nuocsx = data["nuocsx"]
        tl.__tkdien = data["tkdien"]
        tl.__dungtich = data["dungtich"]
        tl.__gia = data["gia"]
        return tl

class C002454:
    @staticmethod
    def testCase1():
        # Tạo tủ lạnh tổng quát tl1 và nhập thông tin
        tl1 = TuLanh()
        tl1.nhapThongTin()
        
        # Tạo tủ lạnh tl2 với các thông số cụ thể
        tl2 = TuLanh(["LG", "LG-28382", "Hàn Quốc", True, 600, 43000000])
        tl2.hienThi()
        
        # Tạo tủ lạnh tl3 sao chép từ tl1
        tl3 = TuLanh(tl1)
        tl3.hienThi()
    
    @staticmethod
    def testCase2():
        # Nhập n tủ lạnh
        n = int(input())
        danhSachTuLanh = []
        
        for i in range(n):
            tl = TuLanh()
            tl.nhapThongTin()
            danhSachTuLanh.append(tl)
        
        # Hiển thị danh sách tủ lạnh theo thứ tự ngược lại
        for i in range(n-1, -1, -1):
            danhSachTuLanh[i].hienThi()
    
    @staticmethod
    def testCase3():
        # Nhập n tủ lạnh
        n = int(input())
        danhSachTuLanh = []
        
        for i in range(n):
            tl = TuLanh()
            tl.nhapThongTin()
            danhSachTuLanh.append(tl)
        
        # Sắp xếp tủ lạnh theo giá giảm dần
        danhSachTuLanh.sort(key=lambda x: x.layGia(), reverse=True)
        
        # Hiển thị danh sách đã sắp xếp
        for tl in danhSachTuLanh:
            tl.hienThi()
    
    @staticmethod
    def testCase4():
        # Nhập n tủ lạnh
        n = int(input())
        danhSachTuLanh = []
        
        for i in range(n):
            tl = TuLanh()
            tl.nhapThongTin()
            danhSachTuLanh.append(tl)
        
        # Lưu danh sách tủ lạnh vào tập tin DsTuLanh.json
        with open("DsTuLanh.json", "w", encoding="utf-8") as f:
            json_data = [tl.to_dict() for tl in danhSachTuLanh]
            json.dump(json_data, f, ensure_ascii=False, indent=4)
    
    @staticmethod
    def testCase5():
        # Nhập n tủ lạnh
        n = int(input())
        danhSachTuLanh = []
        
        for i in range(n):
            tl = TuLanh()
            tl.nhapThongTin()
            danhSachTuLanh.append(tl)
        
        # Thống kê số lượng tủ lạnh theo nhãn hiệu
        counter = Counter([tl.layNhanHieu() for tl in danhSachTuLanh])
        
        # In các nhãn hiệu theo thứ tự ABC
        for nhanhieu in sorted(counter.keys()):
            print(f"{nhanhieu} ({counter[nhanhieu]})")

def main():
    C002454.testCase1()

if __name__ == "__main__":
    main()