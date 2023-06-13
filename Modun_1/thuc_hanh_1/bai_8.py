# Bài 8 :
'''Quy định giá nước máy của tỉnh A được tính như sau: Mỗi người trong một gia đình được sử dụng 4m3
nước với giá 6 000 đồng/m3, 2m3 tiếp theo với giá 8 000 đồng/m3, các m3còn lại tính với giá 12 000 đồng/m3. 
Một hộ gia đình có 5 người, trong một tháng đã sử dụng hết 45m3 nước máy. Hỏi gia đình này phải trả bao nhiêu 
tiền? Biết rằng mỗi gia đình phải đóng thêm thuế giá trị gia tăng và phí bảo vệ môi 
trường là 15%.''' 

# price_1 = 6000
# price_2 = 8000
# price_3 = 12000

# water_1 = 4
# water_2 = 6 
# water_3 =12
# water_person = 5


# w_price = 0

# if water_person <= 4:
#     w_price = water_1 * price_1
# elif water_person in range(4,7):
#     w_price = (water_1 * price_1) + (water_2 * price_2)
# else:
#     w_price = (water_1 * price_1) + (water_2 * price_2) + ((water_person - water_1 - water_2) * price_3)
# print(w_price)
# print("Price : ", w_price * 5 + (w_price * 15 / 100),"vnd")

from audioop import avg


PRICE1 = 6000
PRICE2 = 8000
PRICE3 = 12000
totalWater = int(input('Input total water of a family: '))
people = int(input('Input number of people in a family: '))

avgUnits = totalWater/people
print(avgUnits)

if avgUnits <= 4:
    payAmount = PRICE1*4
elif avgUnits in range(4, 7):
    payAmount = PRICE1*4 + PRICE2*2
else:
    payAmount = PRICE1*4 + PRICE2*2 + PRICE3*(avgUnits-6)

print(payAmount)

pay = payAmount * 5 * (payAmount * 0.15)
print(pay)

