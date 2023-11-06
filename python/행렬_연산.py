def solution(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        temp_list = []
        for j in range(len(arr2[0])):
            temp_val = 0
            for k in range(len(arr2)):
                temp_val += arr1[i][k] * arr2[k][j]
            temp_list.append(temp_val)
        result.append(temp_list)
    return result