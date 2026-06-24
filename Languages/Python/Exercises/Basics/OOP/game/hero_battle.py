from hero import *
from enemy import *
def hero_battle(hero: Hero, enemy: Enemy):
    while hero.health_points>0 and enemy.health_points>0:
        print('---')
        enemy.special_attack()
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage
    
    if hero.health_points >0 :
        print("Hero Wins!")
    else:
        print("Enemy Wins!")