"""Trere are some exception classes for game"""

class EnemyDown(Exception):
    """Run if enemy health equal zero"""
    def __init__(self, msg: str):
        self.msg = msg

class GameOver(Exception):
    """Run if player health iz zero"""
    def __init__(self, msg: str):
        self.msg = msg

