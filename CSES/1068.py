
def run(n):
    if n % 2:
        return (n * 3) + 1
    else:
        return n // 2


def main():

    val = int(input())

    while True:
        print(val, end=" ")

        if val == 1:
            exit()

        val = run(val)

if __name__ == '__main__':
    main()