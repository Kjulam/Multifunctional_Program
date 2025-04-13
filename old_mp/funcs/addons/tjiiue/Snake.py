from funcs.addons.tjiiue.consts import *
import random
class Snake:
    def __init__(self):
        self.body = [INITIAL_POS]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (
            (head_x + dx * CELL_SIZE) % WIDTH,
            (head_y + dy * CELL_SIZE) % HEIGHT
        )

        if new_head in self.body[1:]:
            return False

        self.body.insert(0, new_head) # type: ignore
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        return True

    def change_direction(self, new_dir):
        if (new_dir[0] + self.direction[0] != 0 or
                new_dir[1] + self.direction[1] != 0):
            self.direction = new_dir

