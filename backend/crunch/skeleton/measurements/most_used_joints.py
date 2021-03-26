from helpers import norm_by_array


def most_used_joints(n):
    """ Putting the norm in a list such that
    list[0] = joint 0, list[1] = joint 1 etc.
    :param n: Datapoints
    :type n: list
    :return total: List of most used joint
    :type stabilityList: list
    """
    usedList = []
    mostUsed = 0
    for i in range(len(n) - 1):
        jointNr = 0
        highest = 0
        sum = 0
        for j in range(len(n[i])):
            used = norm_by_array(n[i][j], n[i + 1][j])
            if(highest<=used):
                jointNr = j
            sum += used
        sum = sum/24
        usedList.append((jointNr, sum))
    return usedList


from helpers import array
print(most_used_joints(array(5)))