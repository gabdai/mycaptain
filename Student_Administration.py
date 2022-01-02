import csv
def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Contact number","E-mail ID"])

        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student_num = 1
    while condition:
        student_info = input("enter student information for student #{} in the following formate ( Name Age Contact_number E-mail_ID) :".formate(student_num))

        # split
        student_info_list = student_info.split(' ')

        print("\n Entered information is -\nName: {}\nAge: {}\nContact_number: \nEmail-ID: {} "
                .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
        choice_check = input("is the entered info correct? (yes/no)")

        if choice_check == "yes" :
            write_into_csv(student_info_list)
            condition_check = input("if you want to enter info of another student say yes or no :")
            if condition_check == "yes":
                student_info = True
                student_num = student_num + 1
            elif condition_check == "no":
                student_info = False
        elif choice_check == "no":
            print("\nplease re-enter the info")
