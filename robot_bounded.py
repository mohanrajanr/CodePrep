def isRobotBounded(instructions: str) -> bool:

    x, y = 0, 0
    dx, dy = 0, 1
    for inst in instructions:
        if inst == 'L':
            dx, dy = -dy, dx
        elif inst == 'R':
            dx, dy = dy, -dx
        else:
            x += dx
            y += dy

        print(x, y)

    return (x, y) == 0 or (dx, dy) != (0, 1)


print(isRobotBounded("GGLLGG"))
print(isRobotBounded("GG"))
print(isRobotBounded("GL"))
