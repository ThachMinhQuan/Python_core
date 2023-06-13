# Bài 3:
''' viết chương trình nhập vào 3 số nguyên là 3 cạnh của tam giác kiểm tra xem đó là tam giác gì
vuông , cân ,đều , tính chu vi và diện tích của tam giác '''

from cmath import sqrt
import math
a = float(input(" Nhập vào cạnh đầu tiên : "))
b = float(input(" Nhập vào cạnh thứ 2 : "))
c = float(input(" Nhập vào cạnh thứ 3 :"))

def kiem_tra(a,b,c):
    if a + b > c and b + c > a and c + a > b :
        return True
    else : 
        return False
print(" a ,b , c là 3 cạnh của một tam giác " , kiem_tra(a,b,c))

if kiem_tra(a,b,c):
    if a == b == c:
        print(" Đây là tam giác đều ") 
    elif a == c or a == b or c == b :
        print(" Đây là tam giác cân")
    elif a*a + b*b == c*c or a*a + c*c ==  b*b or  b*b + c*c == a*a:
        print(" Đây là tam giác vuông")
    else:
        print(" Đây là tam giác bình thường")
    p = (a + b +c)/2
    s = sqrt(p*(p-a)*(p-c)*(p-b))
    print(" Chu vi của tam giác là : ", p*2)
    print(" Diện tích của tam giác là : ",s )
else:
    print(" 3 cạnh trên ko phải là ba cạnh của tam giác ")
    