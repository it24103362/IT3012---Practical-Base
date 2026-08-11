import random
from collections import deque


class GreedyGridAgent:
    """A simple agent that tries to move around systematically to clear the grid."""

    def __init__(self):
        self.actions_pool = ['Up', 'Down', 'Left', 'Right']

    def sense_and_act(self, percept: dict) -> str:
        pos = percept['agent_pos']
        return random.choice(self.actions_pool)


class SimpleReflexAgent:
    def sense_and_act(self, percept):
        if percept['food_here']:
            return 'Up'

        if percept['wall_ahead']:
            return 'Right'

        return 'Up'


class ModelBasedAgent:
    def __init__(self):
        self.last_action = 'Up'

    def sense_and_act(self, percept):
        if percept['wall_ahead']:
            self.last_action = 'Right' if self.last_action == 'Up' else 'Up'
            return self.last_action

        return 'Up'


class SearchAgent:

    def bfs_search(self, start, goal, walls, grid_size):
        width, height = grid_size
        walls = set(walls)

        queue = deque([(start, [])])
        visited = {start}

        moves = {
            'Up': (0, 1),
            'Down': (0, -1),
            'Left': (-1, 0),
            'Right': (1, 0)
        }

        while queue:
            (x, y), path = queue.popleft()

            if (x, y) == goal:
                return path

            for action, (dx, dy) in moves.items():
                nx, ny = x + dx, y + dy

                if 0 <= nx < width and 0 <= ny < height:
                    if (nx, ny) not in walls and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append(((nx, ny), path + [action]))

        return None