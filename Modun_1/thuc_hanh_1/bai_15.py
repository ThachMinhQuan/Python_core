# Bài 15:
''':Công ty A cung cấp dịch vụ Internet với mức chi phí ban đầu là 300 000 đồng 
và chi phí trả hàng tháng là 72 000 đồng. Công ty B cung cấp dịch vụ Internet không 
tính chi phí ban đầu, nhưng chi phí trả hàng tháng là 90 000 đồng. Anh Hoàng đã đăng 
ký dịch vụ Internet của công ty A, hỏi anh Hoàng phải sử dụng dịch vụ Internet của 
công ty A ít nhất trong bao lâu thì tổng chi phí sử dụng sẽ rẻ hơn nếu sử dụng của công 
ty B. '''

pay_fA  =    300000
pay_fB  =    0
count   =    0
while(pay_fA >= pay_fB):
    pay_fA  =   pay_fA +  72000 * count
    pay_fB  =   pay_fB +  90000 * count
    count += 1
print(f"Hoàng phải sử dụng dịch vụ Internet của công ty A ít nhất trong {count}" , "ngày")
