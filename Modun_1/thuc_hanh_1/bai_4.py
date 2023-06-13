""" Bài 4: Bác Tư đi taxi của hãng xe A từ Chợ Bến Thành lên TP Biên Hòa, quãng đường
dài 42km. Tiền cước taxi được tính như sau: dưới 500m giá cước 12000 đồng, giá
cước các km tiếp theo là 15000 đồng cho mỗi km, từ km số 31 trở đi thì giá cước mỗi
km là 10000 đồng. Hãy tính xem bác Tư phải trả bao nhiêu tiền cước taxi. (Tiền taxi
bao gồm phí qua trạm BOT là 20000 đồng) """

gia0 = 12000
gia1 = 15000
gia2 = 10000
BOT = 20000
d = 42 #km
d0 = 0.5 #km
d1 = 31

if d<d0:

    t = gia0

elif d<31:

    t = gia0 + (d-d0)*gia1

else:

    t = gia0 + (d1-d0)*gia1 + (d-d1)*gia2

t = t + BOT

print("So tien di taxi la", t, "dong")