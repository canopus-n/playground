# A string is said to be a special string if either of two conditions is met:
#  - All of the characters are the same, e.g. aaa.
#  - All characters except the middle one are the same, e.g. aadaa.
# A special substring is any substring of a string which meets one of those criteria.
# Given a string, determine how many special substrings can be formed from it.

# Complete the substrCount function below.
def substr_count(n, s):
    count = 0
    for row in range(n):
        for col in range(row, n):
            if s[row] == s[col]:
                print('%s == %s, (%d,%d)' % (s[row], s[col], row, col))
                count += 1
            else:
                if s[row:col] == s[col + 1:2 * col - row + 1]:
                    print('%s == %s, (%d,%d) == (%d,%d)' % (
                        s[row:col], s[col + 1:2 * col - row + 1], row, col, col + 1, 2 * col - row + 1
                    ))
                    count += 1
                else:
                    print('%s != %s, (%d,%d) != (%d,%d)' % (
                        s[row:col], s[col + 1:2 * col - row + 1], row, col, col + 1, 2 * col - row + 1
                    ))
                break
    return count


if __name__ == '__main__':
    # result = substrCount(7, 'abcbaba')
    # result = substrCount(5, 'asasd')
    result = substr_count(25, 'aaaadaaaccccccxcccccfcccc')

    print(result)