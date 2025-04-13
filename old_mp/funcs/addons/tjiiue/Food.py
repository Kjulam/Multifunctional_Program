import random
from funcs.addons.tjiiue.consts import *

def new_position(snake):
    while True:
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        if (x, y) not in snake.body:
            return (x, y)

class Food:
    def __init__(self, snake):
        self.position = new_position(snake)

