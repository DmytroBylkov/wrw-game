
class EnemyDown(Exception):
    """Run if enemy health equal zero"""
    def __init__(self, msg: str):
        self.msg = msg
    

class GameOver(Exception):
    """Run if player health iz zero"""
    def __init__(self, msg: str):
        self.msg = msg

class KeyboardInterrupt(Exception):
    """run if player push enter without number"""
    def __init__(self, msg: str):
        self.msg = msg
