from typing import List
import collections


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    pop_list = collections.deque(popped)
    push_list = collections.deque(pushed)

    stack = []
    while push_list:
        n = push_list.popleft()

        if n == pop_list[0]:
            pop_list.popleft()

        else:
            while stack and stack[-1] == pop_list[0]:
                stack.pop()
                pop_list.popleft()

            stack.append(n)

    while stack and stack[-1] == pop_list[0]:
        stack.pop()
        pop_list.popleft()

    return len(pop_list) == 0

print(validateStackSequences([2, 1, 0], [1, 2, 0]))
print(validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
print(validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))