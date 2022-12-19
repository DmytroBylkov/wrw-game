"""Here starting game"""
from models import Player, Enemy
from exception import EnemyDown, GameOver

def get_player_name() -> str:
    """get player name from user input """
    player_name = input("Enter your name for play: ").strip()
    while len(player_name) < 1:
        print("You must enter at least one character for the game name")
        player_name = input("Enter your name for play: ").strip()
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
        except EnemyDown as enemydown:
            print(enemydown)
            enemy = Enemy()
        except GameOver as gameover:
            print(gameover)
            print(f"{player.name} end game with score = {player.score }")
            break

     
if __name__ == "__main__":
    try:
        play()
    except KeyboardInterrupt("Oops, you enter empty value") as truble:
        print(truble)
