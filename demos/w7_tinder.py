def interest():
    print("Enter all interests, one after another or \"STOP\": ")
    s1 = set()
    interest = ""
    while True:
        interest = input()
        if interest.lower() == "stop":
            break
        s1.add(interest)
    return s1

def run():
    print("First person: ")
    p1 = interest()
    print("Second person: ")
    p2 = interest()
    common = p1.intersection(p2)
    if len(common) >= 3:
        print(f"You are a match made in heaven! You have {len(common)} hobbies in common")
    else:
        print("Oh no! It will probably not work. Find another human.")

run()