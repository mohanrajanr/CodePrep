from typing import List


def asteroidCollision(asteroids: List[int]) -> List[int]:
    st = []

    for a in asteroids:

        while st and a < 0 and st[-1] > 0:

            if st[-1] == -a:
                st.pop()
                break

            elif st[-1] < -a:
                st.pop()
                continue

            else:
                break

        else:
            st.append(a)

    return st


print(asteroidCollision([5,10,-5]))
print(asteroidCollision([8,-8]))
print(asteroidCollision([8,-9]))
print(asteroidCollision([10, 2, -5]))
print(asteroidCollision([-2, -1, 1, 2]))