def email_process(email_name):
    ten_nguoi_dung = email_name[0:email_name.index("@")]
    dia_chi_email = email_name[email_name.index("@") + 1:]
    return ten_nguoi_dung , dia_chi_email

def print_email(ten_nguoi_dung , dia_chi_email):
    print(f"Tên người dùng là : {ten_nguoi_dung}")
    print(f"Tên địa chỉ email là : " {dia_chi_email})



def main():    
    email_name = input(" Nhập vào email của bạn : ").strip()
    email_process(email_name)
    print_email(ten_nguoi_dung ,dia_chi_email)
    print(f"Email của bạn là {email_name}")

if __name__ == "__main__":
    main()