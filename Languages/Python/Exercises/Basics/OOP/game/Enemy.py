class Enemy:
    __type_of_enemy: str
    health_points: int=10
    attack_damage: int=1

    def __init__(self):
        print('New enemy created with no starting values')
    
    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self.__type_of_enemy: str = type_of_enemy
        self.health_points: int=health_points
        self.attack_damage: int=attack_damage
        print(f'New enemy {self.__type_of_enemy} created with {self.attack_damage} attack values!')

    def talk(self):
        print(f'I am a {self.__type_of_enemy}. Be prepared to fight')

    def walk_forward(self):
        print(f'{self.__type_of_enemy} moves close to you')
    
    def attack(self):
        print(f'{self.__type_of_enemy} attacks for {self.attack_damage}')

    def get_type_of_enemy(self):
        return self.__type_of_enemy
    
    def special_attack(self):
        print(f'{self.__type_of_enemy} does not have special attack')