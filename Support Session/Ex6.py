import csv
stud_id = 1001
#global variable -> visible to all functions

def generate():
    name = input("Enter name: ")
    dob = input("Enter date of birth: ")
    age = int(input("Enter age"))
    global stud_id
    stud_id += 1
    return name, dob, age, stud_id

def saving(students=[], mode="a"):
    with open("students.csv", mode, newline="") as f:
        csv_writer = csv.writer(f)
        for bob in students:
            csv_writer.writerow(bob)
#[(),(),(),(),(),()]

def loading(path):
    stud_list = []
    with open(path) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            if len(row) > 0:
                stud_list.append(tuple(row))
    return stud_list

def run():
    student_list = loading("students.csv")
    while True:
        print("Menu\n1-Add Student\n2-Show all\n0-Exit")
        opt = int(input())
        if opt == 1:
            stud = generate()
            student_list.append(stud)
            saving(student_list, "w")
        elif opt == 2:
            print(student_list)
        elif opt == 0:
            break

run()

#print(loading("students.csv"))
# t= generate(), generate(), generate()
# ss = list(t)
# saving(ss)