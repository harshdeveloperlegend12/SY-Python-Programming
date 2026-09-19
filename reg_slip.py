def reg_slip(name, reg_no, subject):
    print("\n===================================")
    print("      ONLINE EXAMINATION PORTAL")
    print("         REGISTRATION SLIP")
    print("===================================")
    print("Student Name       :", name)
    print("Registration No.   :", reg_no)
    print("Exam Subject       :", subject)
    print("===================================")

name = input("Enter Student Name: ")
reg_no = int(input("Enter Registration Number: "))
subject = input("Enter Examination Subject: ")

reg_slip(name, reg_no, subject)