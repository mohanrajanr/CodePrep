def runner(*args, **kwargs):
    a_val = args[0]
    n = args[1]
    k = args[2]

    shifts = 0

    # Find Max Val
    max_val = a_val
    for i in range(n):
        a_val = a_val[1:] + a_val[0]

        if int(max_val, 2) < int(a_val, 2):
            max_val = a_val
        shifts += 1

    k -= 1



def main():
    test_cases = int(input())

    while test_cases:
        test_cases -= 1

        n, k = map(int, input().split())

        a_val = input()
        print(runner(a_val, n, k))

if __name__ == '__main__':
    main()