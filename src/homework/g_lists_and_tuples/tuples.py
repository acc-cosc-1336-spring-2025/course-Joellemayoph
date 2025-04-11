
def get_p_distance(list1, list2):

    pdistance = 0 

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            pdistance += 1.00

    pdistance = pdistance/len(list1)

    return pdistance


def get_p_distance_matrix(list1):
    lista = [item for item in list1[0]]
    listb = [item for item in list1[1]]
    listc = [item for item in list1[2]]
    listd = [item for item in list1[3]]

    masterlist = ([lista] + [listb] + [listc] + [listd])

    row = len(masterlist)
    col = len(masterlist[0])

    matrix = []
    for index in range(row):
        rows = []
        for j in range(row):
            rows.append(0.0)
        matrix.append(rows)

    for i in range(row):
        for j in range(row):
            pdist = get_p_distance(masterlist[i], masterlist[j])
            matrix[i][j] = pdist
                
    return matrix


