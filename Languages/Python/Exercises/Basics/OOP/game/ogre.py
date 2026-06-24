from enemy import *
import random
"""
Enemy Ogre class
"""
class Ogre(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__('Ogre', health_points, attack_damage)

    def talk(self):
        print('Ogre is slamming hands all around!')

    def special_attack(self):
        attack_points = 4;
        did_special_attack_work = random.random() < 0.2
        if did_special_attack_work:
            self.attack_damage +=attack_points
            print(f'Ogre attack points increased by {attack_points}')