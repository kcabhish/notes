from Enemy import *
enemy = Enemy()
enemy.type_of_enemy = 'Zombies'
print(f'{enemy.type_of_enemy} has {enemy.health_points} health points And can do attack of {enemy.attack_damage}')
enemy.talk()