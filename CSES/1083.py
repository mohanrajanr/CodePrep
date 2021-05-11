
def main():

    total = int(input())
    array = map(int, input().split())

    miss = (total * (total + 1))//2 - sum(list(array))
    print(miss)

if __name__ == '__main__':
    main()
