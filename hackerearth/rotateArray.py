import math


def main():
    test_cases = int(input())

    while test_cases:
        test_cases -= 1

        n, k = map(int, input().split())
        k = k % n

        arr = list(map(int, input().split()))

        for i in range(math.gcd(k, n)):

            temp = arr[i]
            j = i
            while True:
                s = (j - k) % n
                if s == i:
                    break
                arr[s], arr[j] = arr[j], arr[s]
                j = s
            arr[j] = temp

        print(arr)

if __name__ == '__main__':
    main()