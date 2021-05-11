from typing import List


def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:

    boxTypes.sort(key=lambda x: -x[1])
    # print(boxTypes)

    index = 0
    boxes = 0
    units = 0
    remaining = truckSize
    while index < len(boxTypes) and remaining > 0:
        # print(boxes, units, remaining, boxTypes[index])
        if boxTypes[index][0] <= remaining:
            boxes += boxTypes[index][0]
            units += boxTypes[index][0] * boxTypes[index][1]
            remaining -= boxTypes[index][0]
            index += 1
        else:
            boxes += remaining
            units += remaining * boxTypes[index][1]
            # print(boxes, units, boxTypes[index])
            break

    return units


print(maximumUnits([[1,3],[2,2],[3,1]], 4))
