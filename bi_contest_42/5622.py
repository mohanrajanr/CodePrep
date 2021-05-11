
def averageWaitingTime(customers: list) -> float:

    finishing_time = 0
    sum_time = 0
    for customer in customers:
        arrival = customer[0]
        finishing_time = max(arrival + customer[1], finishing_time + customer[1])

        sum_time += finishing_time - arrival

    return sum_time/len(customers)

# Test Cases
print(averageWaitingTime([[1,2],[2,5],[4,3]]))
print(averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))