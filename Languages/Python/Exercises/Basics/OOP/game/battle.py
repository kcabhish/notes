from enemy import *
from hero import *
"""
Battle method to make the 2 enemies fight
"""
def battle(e1: Enemy | Hero, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        # initiate special_attack at the beginning of the battle
        e1.special_attack()
        e2.special_attack()

        if e2.health_points>0:
            e2.attack()
            e1.health_points -= e2.attack_damage

        if e1.health_points>0:
            e1.attack()
            e2.health_points -= e1.attack_damage
        
    if (e1.health_points > 0):
        print(f'{e1.get_type_of_enemy()} wins the battle!')
    else:
         print(f'{e2.get_type_of_enemy()} wins the battle!')