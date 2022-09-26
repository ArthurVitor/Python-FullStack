from enum import Enum

class Directions(Enum):
    right = 0
    left = 1


def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError('Cannot move in this direction')
    return f'Moving {direction.name}'

if __name__ == '__main__':
    print(move(Directions.right))
    print(move(Directions.left))
    print(move(Directions.up))