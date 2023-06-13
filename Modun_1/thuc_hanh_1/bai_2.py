 # Bài 2:
'''
 Nhập vào danh sách học sinh gồm họ tên, năm sinh, giới tính, điểm Toán, điểm Anh,
 điểm Văn, Điểm TB = (điểm Toán + điểm Anh+ điểm Văn)/3. 
 Yêu cầu:
 a) Xếp loại học lực của học sinh dựa vào điểm TB:
 Xuất sắc: ĐTB>=9
 Giỏi: ĐTB>=8
 Khá: ĐTB>=7
 TB: ĐTB<7
 b) In ra danh sách học sinh theo TT giảm dần của điểm TB'''

i=0
students={}
action = 'y'

#---------------------------------------------------------------------------

def xeploai(x):
    if x >=9: return 'Xuất sắc'
    elif x >=8: return 'Giỏi'
    elif x >=7: return 'Khá'
    else: return 'Trung bình'

#---------------------------------------------------------------------------------
while action =='y': #mục xử lý nhập

    name = input('Nhập tên học sinh:')
    year=input('Nhập năm sinh:')
    sex=input('Nhập giới tính của học sinh (ghi rõ nam hoặc nu):')
    math = int(input('Nhập điểm toán:'))
    eng=int(input('Nhập điểm tiếng anh:'))
    lite=int(input('Nhập điểm môn văn:'))
    med=round((math+eng+lite)/3,2)
    xl = xeploai(med)

    student = {'name':name,'year':year,'sex':sex,'math':math,'eng':eng,'lite':lite,'med': med,'xl':xl}
    action=input('Nếu bạn đã nhập xong, bấm enter để lưu lại, nếu muốn nhập thêm hãy bấm "y":')
    students[i]=student; i+=1

#   print(students)

#--------------------------------------------------------------------
kt = []
for x in students:
    kt.append((students[x]['med'],students[x]['name']))  # tạo list từ dic và sắp xếp
kt.sort(reverse=True)

print('\nDanh sách học sinh có điểm trung bình từ cao đến thấp là:')
for x in range(len(kt)):
    print(x+1,'.  ', kt[x][1],' -- Điểm trung bình là:  ',kt[x][0])
