from models import Player, Enemy
from exception import EnemyDown, GameOver


def get_player_name() -> str:
    """get player name from user input """
    player_name = input("Enter your name for play: ")
    return player_name


def play() -> None:
    """Main loop for game"""
    
    player_name = get_player_name()
    player = Player(player_name)
    enemy = Enemy()

    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except EnemyDown as exc:
            print(exc)
            enemy = Enemy()
        except GameOver as exc:
            print(exc)
            print(f"{player.name} end game with score = {player.score }")
            break

       


if __name__ == "__main__":
    try:
        play()
    except KeyboardInterrupt("Oops, you enter empty value") as exc:
        print(exc)