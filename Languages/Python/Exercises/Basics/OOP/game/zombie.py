"""
Zombie class is a child of Enemy
"""
from enemy import *
import random
class Zombie(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__('Zombie', health_points, attack_damage)

    def talk(self):
        print('* Grumbling...*')
    
    def spread_disease(self):
        print('The Zombie is trying to spread infection')

    def special_attack(self):
        health_regenerated = 2;
        did_special_attack_work = random.random() < 0.5
        if did_special_attack_work:
            self.health_points +=health_regenerated
            print(f'Zombie regenerated {health_regenerated} HP!')