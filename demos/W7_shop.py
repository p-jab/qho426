import json

def shop():
    with open("shop.json") as f:
        items = json.load(f)
    return items
print(shop())

def save_json(dictio={}):
    with open("shop.json", "w") as f:
        json.dump(dictio, f)

def view_all(products={}):
    for x, y in products.items():
        print(f"{x}----------£{y}")

def basket():
    b = []
    while True:
        p = input("Enter an item or \"stop\": ")
        if p.upper() == "STOP":
            break
        q = int(input(f"Enter the quantity of {p}: "))
        for i in range(q):
            b.append(p)
    return b

def till(basket=[]):
    all_items = shop()
    total = 0
    for prod in basket:
        if prod.lower() in all_items:
            total += all_items[prod]
        else:
            print(f"No luck. The {prod} is not in stock. Go to LIDL")
    return total

def run():
    print("Welcome to Piotr's shop. Please look around. We are watching you.")
    view_all(shop())
    b = basket()
    while True:
        response = input("Are you ready to pay [y/n]: ")
        if "y" in response.lower():
            to_pay = till(b)
            print(f"Pay £{to_pay} or I will come after you!")
            break
        else:
            b2 = basket()
            b.extend(b2)

