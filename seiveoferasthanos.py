def seiveOfEratosthenes(number: int) -> list:
    seive = [0 for i in range(number + 1)]
    prime_nums = []

    for i in range(2, number + 1):
        # Its a prime number
        if seive[i] == 0:
            seive[i] = i
            prime_nums.append(i)

        for j in prime_nums:
            # Do Work till Minimum Prime Factor or
            # till when Number * prime number > input number
            if j > seive[i] or i * j > number:
                break

            # print("Doing for {} for {} gives: {}".format(j, i, i*j))
            seive[i * j] = j

    return prime_nums

print(seiveOfEratosthenes(11373))