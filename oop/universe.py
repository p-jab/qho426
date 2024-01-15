from planet import Planet
from human import Human
from robot import Robot
import random
import matplotlib.pyplot as plt


class Universe:

    def __init__(self):
        self.planets = []


    def generate(self):
        p = Planet("Earth")
        random_num = random.randint(1, 10)
        for i in range(random_num):
            h = Human()
            p.add(h)
        random_num = random.randint(1, 10)
        for i in range(random_num):
            r = Robot()
            p.add(r)
        self.planets.append(p)

    def show_populations(self, selection):
        x_values = []
        y_values = []
        i = 1
        for planet in self.planets:
            if selection.lower() == "human":
                num_hum = 0
                for dude in planet.inhabitants:
                    if isinstance(dude, Human):
                        num_hum += 1
                y = num_hum
            elif selection.lower() == "robot":
                num_rob = 0
                for dude in planet.inhabitants:
                    if isinstance(dude, Robot):
                        num_rob += 1
                y = num_rob
            else:
                y = len(planet.inhabitants)
            x_values.append(f"Planet {i}")
            y_values.append(y)
            i += 1
        plt.bar(x_values, y_values)
        plt.show()


if __name__ == "__main__":
    u = Universe()
    for i in range(3):
        u.generate()
    u.show_populations("human")
