numbers = [0, 1,2, 3,4,6, 5]



for i in numbers:

    print(i)

print("That is all in numbers list.")



for i in numbers:

    print(i)

    if i==1: break

else:    

    print("That is all in numbers list.")




tong=0

for i in numbers:

    print(i)

    tong = tong + i

else:    

    print("Tong = ",tong)  



tong=0

for i in numbers:

    print(i)

    tong = (tong + i)
print("Tong = ",tong)
tong = 0

for i in numbers:


    if i%2==0: tong = tong + i

   

print("Tong chan = ",tong)
tong = 0

for i in numbers:

    if i%2==0: tong = tong + i

else: print("Tong chan = ",tong)
tong = 0
dem = 0
for i in numbers:
    if i%2==0:

        tong = tong + i

        dem = dem + 1
else:
    print("So cac cho chan: ",dem)

    print("Trung binh cong cac so chan = %.2f"%(tong/dem))