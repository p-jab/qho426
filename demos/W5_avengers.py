def adding(lista=[]):
    new_member = input("Enter name of new avenger: ")
    lista.append(new_member)


def remove(lista=[]):
    name = input("enter name of avenger to be removed: ")
    if name in lista:
        lista.remove(name)


def printing(lista=[]):
    for thing in lista:
        print(f"The mighty {thing} is part of avengers!")


def run():
    avengers = []
    while True:
        opt = int(input(
            '''Avengers, Assemble!
    1-Add an Avenger
    2-Remove and Avenger
    3-Check the team
    4-Exit                       
                '''))
        if opt == 1:
            adding(avengers)
        elif opt == 2:
            remove(avengers)
        elif opt == 3:
            printing(avengers)
        elif opt == 4:
            break
        else:
            print("No such option. Go SpecSavers!")

run()