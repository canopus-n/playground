

def lcs(s1, s2):
    curr_row = [0] * (len(s2)+1)
    prev_row = [0] * (len(s2)+1)
    for s_i in s1:
        for j, s_j in enumerate(s2, 1):
            if s_i == s_j:
                curr_row[j] = prev_row[j-1] + 1
            else:
                curr_row[j] = max(prev_row[j], curr_row[j-1])
        prev_row, curr_row = curr_row, prev_row
        print(prev_row)
    return prev_row[-1]


if __name__ == '__main__':
    s1 = 'WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS'
    s2 = 'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'
    # s1 = 'SHINCHAN'
    # s2 = 'NOHARAAA'
    # s1 = 'AA'
    # s2 = 'BB'

    result = lcs(s1, s2)
    print(result)




