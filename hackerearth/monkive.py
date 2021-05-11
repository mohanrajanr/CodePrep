import math


def main():
    test_cases = int(input())

    while test_cases:
        test_cases -= 1

        n = int(input())

        arr = []
        for i in range(n):
            arr.append(list(map(int, input().split())))

        cases = [(i, j) for i in range(n) for j in range(n)]
        difference = 0
        for x, y in cases:
            for i, j in cases:
                if x > i or y > j:
                    continue
                if arr[x][y] > arr[i][j]:
                    difference += 1

        print(difference)

if __name__ == '__main__':
    main()