from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:

    intervals.sort(key=lambda x: x[0])
    curr = intervals[0]
    result = []

    for i in range(1, len(intervals)):
        selected = intervals[i]

        # print(curr, selected)

        if selected[0] < curr[0] and curr[1] < selected[1]:
            # Absorbed
            curr = selected

        elif curr[0] < selected[0] and curr[1] > selected[1]:
            # dissolve
            continue

        elif curr[1] < selected[0]:
            # Append
            result.append(curr)
            curr = selected

        elif curr[1] == selected[0]:
            # Extend
            curr[1] = selected[1]

        elif selected[0] < curr[0]:
            curr[0] = selected[0]

        elif curr[1] < selected[1]:
            curr[1] = selected[1]
        else:
            print("error")

    result.append(curr)
    return result


print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))
print(merge([[1,4],[0,0]]))