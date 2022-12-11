"""Here descreabe two classes for game Enemy and Player"""
import random
from exception import EnemyDown, GameOver
from settings import LIST_OF_VARIANTS, INITIAL_PLAYER_HEALTH

class Enemy():
    """create opponent for play"""

    health = 0

    def __init__(self):
        """enemy stats"""
        Enemy.health += 1

    def descrease_health(self):
        """decrease enemy health by 1"""
        self.health = self.health - 1
        if self.health < 1:
            raise EnemyDown("You win your enemy")
        return self.health

    def select_attack(self):
        """random choise from list """
        choise_enemy_attack = LIST_OF_VARIANTS[random.randint(0, 2)]
        return choise_enemy_attack

    def select_defence(self):
        """random choise from list"""
        choise_enemy_defence = LIST_OF_VARIANTS[random.randint(0, 2)]
        return choise_enemy_defence

class Player():
    """create player for game"""

    def __init__(self, name):
        """player stats"""
        self.name = name
        self.player_health = INITIAL_PLAYER_HEALTH
        self.score = 0

    def descrease_health(self):
        """decrease plaayer health by 1"""
        self.player_health = self.player_health - 1
        if self.player_health < 1:
            raise GameOver ("You lose")
        return self.player_health

    def select_attack(self):
        """return fight choise"""
        try:
            attack_choise = LIST_OF_VARIANTS[int(input("Select your attack_choise(1 - WARRIOR, 2 - ROBBER, 3 - WIZARD: ")) - 1]
            return attack_choise
        except IndexError:
            print("You must input only 1, 2 or 3")
            self.select_attack()

    def select_defence(self):
        """return defence choice"""
        try:
            defence_choise = LIST_OF_VARIANTS[int(input("Select your defence_choise(1 - WARRIOR, 2 - ROBBER, 3 - WIZARD: ")) - 1]
            return defence_choise
        except IndexError:
            print("You must input only 1, 2 or 3")
            self.select_defence()

    def attack(self, other: Enemy):
        """for attack enemy"""
        player = self.select_attack()
        enemy = other.select_defence()
        if player == "WARRIOR" and enemy == "ROBBER" \
        or player == "ROBBER" and enemy == "WIZARD" \
        or player == "WIZARD" and enemy == "WARRIOR":
            self.score += 1
            other.descrease_health()
            return  print("YOUR ATTACK IS SUCCESSFUL!")
        elif player == enemy:
            return print("IT'S A DRAW!")
        else:
            return print("YOUR ATTACK IS FAILED!")

    def defence(self, other:Enemy):
        """for defence from enemy attack"""
        player = self.select_defence()
        enemy = other.select_attack()
        if player == "WARRIOR" and enemy == "ROBBER" \
        or player == "ROBBER" and enemy == "WIZARD" \
        or player == "WIZARD" and enemy == "WARRIOR":
            return print("YOUR DEFENCE IS SUCCESSFUL!")
        elif player == enemy:
            return print("IT'S A DRAW!")
        else:
            self.descrease_health()
            return print(f"YOUR DEFENCE IS FAILED! Your health - {self.player_health}")

if __name__ == "__main__":
    enemy2 = Enemy()
    print(enemy2.health, enemy2.select_attack(), enemy2.select_defence())
    player2 = Player("testing")
    enemy1 = Enemy()
    print(enemy1.health)
