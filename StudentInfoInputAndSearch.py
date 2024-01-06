studentCount = int(input("Enter number of students: "))
i = 0
studentRecord = dict()

while i < studentCount:
    name, marks = input("Enter student name and marks separated by space: ").split()
    marks = int(marks)
    studentRecord[name] = marks
    i += 1

while True:
    nameToSearch = input("Give the name to search the marks: ")

    if nameToSearch in studentRecord:
        print(f"Marks for {nameToSearch}: {studentRecord[nameToSearch]}.")
    else:
        print("Marks unavailable")

    option = input("Do you want to search another student? (Yes/No): ")

    if option.lower() == "no":
        print("Thank you for using.")
        break  # Exit the loop if the user chooses not to search another student
