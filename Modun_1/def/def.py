#  Viết hàm kiểm tra số nguyên dương là số hoàn hảo

def so_hoan_hao(a):
    tam = 0
    for i in range(1,a):
        if a % i == 0 :
            tam = tam + i
    if tam == a or a == 1:
        return True
    else :
        return False
print("Số 6 có phải là số hoàn hảo không : " ,so_hoan_hao(6))

# Viết hàm kiểm tra số nguyên dương là số nguyên tố

def so_nguyen_to(b):
    kt = True
    for i in range(2,b):
        if b%i == 0:
            kt = False
            break
    if kt :
        return True
    else:
        return False
print(" Số 5 có phải là số nguyên tố ko : ",so_nguyen_to(5))

print(" Các số nguyên tố nằm trong đoạn từ 1..50 : ")
for i in range(50):
    if so_nguyen_to(i):
        print(i, end=' ')