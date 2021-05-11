def countStudents(students, sandwiches):
    students = students[::-1]
    sandwiches = sandwiches[::-1]

    startRotate = 0
    while len(sandwiches):

        if students[-1] == sandwiches[-1]:
            students.pop()
            sandwiches.pop()
            startRotate = 0
        else:
            if startRotate >= len(sandwiches):
                break
            students.insert(0, students.pop())
            startRotate += 1

    return len(sandwiches)


print(countStudents([1,1,0,0], [0,1,0,1]))
print(countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))