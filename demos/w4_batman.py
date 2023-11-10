from random import randint

def batman_punch(str = 5, technique = 5):
    punch_power = 0.3*str + 0.7*technique
    return punch_power

def fight_scene(n=2, enemy_str=3):
    total_str = n*enemy_str
    bat_str = batman_punch(randint(0,10), randint(0,10))
    if bat_str >= total_str:
        return "Batman Wins!"
    else:
        return "Batman is Beaten!"

def roberry_escape(n_cars):
    if n_cars > 5:
        return "Batman is caught"
    else:
        return "Batman escapes"

def run():
    escape = roberry_escape(randint(1,10))
    scene = fight_scene(randint(1,5), randint(0, 4))
    print(f"After a long fight, {scene} Afterwards, police chase him and {escape}")

run()