import collections


def main():
    array = input()
    occur = 1
    maxans = 1

    for i in range(1, len(array)):
        if array[i] == array[i-1]:
            occur += 1
            maxans = max(maxans, occur)
        else:
            occur = 1

    print(maxans)

if __name__ == '__main__':
    main()
