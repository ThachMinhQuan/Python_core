# Bài 11:
'''Giá tiền điện hàng tháng ở nhà Minh được tính như sau: 
 Mức 1: tính cho 100kW đầu tiên. 
 Mức 2: tính cho số kW điện từ 101kW đến 150kW, mỗi kW ở mức 2 đắt hơn 150 đồng so với mức 1. 
 Mức 3: tính cho số kW điện từ 151kW đến 200kW, mỗi kW ở mức 3 đắt hơn 200 đồng so với mức 2. 
 Mức 4: từ kW thứ 201 tính chung 1 giá, mỗi kW ở mức 4 đắt hơn so với mức 3 là 250 đồng. 
Ngoài ra, người sử dụng còn phải trả thêm 10% thuế giá trị gia tăng.Tháng vừa rồi nhà Minh dùng hết 165kW điện và phải trả 95 700 đồng. Hãy 
tính xem mỗi kW điện ở mức 1 giá bao nhiêu tiền?'''

price_1  =   0
add_2    =    150
add_3    =    add_2 +  200
add_4    =    add_3 +  250

pay     =   95700  #vnd
consume =   165     #kW
def cal_price1(pay,consume):
    if consume<=100:
        price_1  = (pay/1.1) / consume
    elif consume in range(101,151):
        price_1  = ((pay/1.1) - add_2*(consume-100)) / consume
    elif consume in range(151,200):
        price_1  = ((pay/1.1) - 50*add_2 - add_3*(consume - 150)) / consume
    else:
        price_1  = (pay*1.1 - 50*(add_2 + add_3) - add_4*(consume - 200)) / consume
    print((price_1))

cal_price1(pay, consume)

