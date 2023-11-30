def generate():
    name = input("Enter the name: ")
    mrk = float(input("Enter the mark: "))
    return name, mrk


def list_of_std(n):
    stud_list = []
    for i in range(n):
        stud_list.append(generate())
    return stud_list


def average(lista=[]):
    total = 0
    for item in lista:
        total += item[1]
    avg = total / len(lista)
    return avg


def run():
    s_list = []
    while True:
        opt = int(input(
            "Menu:\n\n1-Populate list of Students\n2-Calculate AVG mark\n3-Change mark of one student\n4-Exit\nChoice: "))
        if opt == 4:
            break
        elif opt == 1:
            num = int(input("How many students to add? "))
            s_list.extend(list_of_std(num))
        elif opt == 2:
            print(f"The average mark is {average(s_list):.2f}")
        elif opt == 3:
            name = input("Whose marks shall we change? ")
            for tup in s_list:
                if tup[0] == name:
                    n_mrk = float(input("Enter new mark: "))
                    s_list.remove(tup)
                    # s_list.append((name, n_mrk))
                    s_list.insert(0, (name, n_mrk))
                    # break
        else:
            print("No such option, try again. Fool!")


run()
