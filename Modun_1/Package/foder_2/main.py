#main.py
import sys

d0 = sys.path
print(sys.path)
d1 ="Python/Package/foder_1"
#print(sys.path)
d0.insert(0, d0 and d1)

from def_1 import *

odd_even(5)
odd_even(8)
print("Tong cua 2 so:", add(6,2))
print("Thuong cua 2 so:", divide(6,2))
print("Tich cua 2 so:", multiple(6,2))