# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN,
# LEFT and RIGHT with a given steps.
import math
position = [0, 0]
while True:
    user_input = input()
    if not user_input:
        break
    movement = user_input.split()
    print(movement)
    direction = movement[0]
    steps = int(movement[1])
    if direction == 'UP':
        position[1] += steps
    elif direction == 'DOWN':
        position[1] -= steps
    elif direction == 'LEFT':
        position[0] -= steps
    elif direction == 'RIGHT':
        position[0] += steps
    else:
        pass

print(int(round(math.sqrt(position[0]**2 + position[1]**2))))