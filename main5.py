attendance = int(input("Enter the number of classes attended: "))
project = int(input("Enter the number of project done: "))
min_project = 70
min_attendance = 75
if project >= min_project and attendance >= min_attendance:
    print("You are eligible for the exam")
else:
    print("You are not eligible for the exam")