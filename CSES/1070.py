
def main():

    number = int(input())

    if number == 1:
        print("1")
        return

    if number < 4:
        print("NO SOLUTION")
        return

    if number % 2:

        for i in range(1, number+1, 2):
            print(i, end=" ")
        for i in range(2, number, 2):
            print(i, end=" ")

    else:
        for i in range(2, number+1, 2):
            print(i, end=" ")
        for i in range(1, number, 2):
            print(i, end=" ")


if __name__ == '__main__':
    main()
