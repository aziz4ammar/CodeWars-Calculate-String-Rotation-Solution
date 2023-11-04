def shifted_diff(first, second):
    if len(first) != len(second):
        return -1

    for i in range(len(first)):
        if first == second:
            return i
        second = second[1:] + second[0]

    return -1