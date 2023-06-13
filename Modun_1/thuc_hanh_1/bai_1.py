# Bài 1:
''' Nhập vào tháng và năm , cho biết tháng năm đó có bao nhiêu ngày'''

thang = int(input("Nhap thang: "))

nam = int(input("Nhap nam: "))
def checkYear(nam):
    if nam % 4 == 0 and nam % 100 != 0 or nam % 400 == 0:

        return True

    else:

        return False

match thang:

    case (1|3|5|7|8|10|12):

        print ("Thang",thang,"nam",nam,"co 31 ngay.")

    case (4|6|9|11):

        print ("Thang",thang,"nam",nam,"co 30 ngay.")        

    case 2:

        if checkYear(nam):

            print ("Thang",thang,"nam",nam,"co 29 ngay.")            

        else:

            print ("Thang",thang,"nam",nam,"co 28 ngay.")          

    case _: #Mặc định

        print ("Khong phai thang trong nam!")
