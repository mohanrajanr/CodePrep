def main():
    total = int(input())
    array = list(map(int, input().split()))

    min_ch = 0

    for i in range(1, total):
        if array[i] < array[i-1]:
            min_ch += (array[i-1] - array[i])
            array[i] = array[i-1]

    print(min_ch)

if __name__ == '__main__':
    main()
