
from enemy import *
from zombie import *
from ogre import *

from hero import *
from weapon import *

from battle import *
from hero_battle import *

zombie = Zombie(10,2)
ogre = Ogre(15,3)

battle(zombie, ogre)
