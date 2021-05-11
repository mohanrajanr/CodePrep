
def is_possible(w, h, n):
    cut = 1
    while h > 1:
        h = h // 2
        cut += 1
    while w > 1:
        w = w // 2
        cut += 1
    return cut + 1 >= n


def main():
    t = int(input())

    while t:
        t -= 1

        w, h, n = list(map(int, input().split()))
        print(is_possible(w, h, n))


if __name__ == '__main__':
    main()
