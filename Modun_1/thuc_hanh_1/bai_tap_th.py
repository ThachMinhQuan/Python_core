import numpy as np
# Viết chương trình tính trung bình cộng các số chẵn và chia hết cho 3 trong đoạn 1..50
sum = 0
dem = 0
for i in range(1,51):
    if i%2 == 0 and i%3 ==0:
        sum = sum + i
        dem = dem + 1
print("Trung bình cộng là : " , float(sum/dem))


# Đếm trong đoạn từ 1..50 có bao nhiêu số chính phương
dem_2 = 0
for i in range(1,50):
    if i == (int(np.sqrt(i)) * int(np.sqrt(i))):
        dem_2 = dem_2 + 1
print(dem_2)

# In ra màn hình các số có tận cùng bằng 3 trong đoạn từ 1..50
print("các sô tận cùng là 3 là : " )
for a in range(1,51):
    if a%10==3:
        print(a , end=" ")


# Tính tích các số hoàn hảo trong đoạn từ 1..50

tich = 1 
for i in range(1,51):
    tong_tam = 0
    #  Mỗi giá trị i : tính tổng các chữ số của nó rồi so sáng với i
    for j in range(1,i):
        if i%j==0:
            tong_tam = tong_tam + j
    if tong_tam == i or i == 1:
        tich = tich * i
        print(i, end=' ')
print("Tính tích các số hoàn hảo trong đoạn từ 1..50 là : ",tich)