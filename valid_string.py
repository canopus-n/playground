# Sherlock considers a string to be valid if all characters of the string appear the same number of times.
# It is also valid if he can remove just 1 character at any 1 index in the string, and the remaining characters
# will occur the same number of times. Given a string , determine if it is valid.
# If so, return YES, otherwise return NO.

def is_valid(s):
    data_by_freq = dict()
    freq_of_data = dict()
    for c in s:
        freq_of_data[c] = freq_of_data.get(c, 0) + 1
    for c, freq in freq_of_data.items():
        if freq not in data_by_freq:
            data_by_freq[freq] = [c]
        else:
            data_by_freq[freq].append(c)
    print(data_by_freq)
    if len(data_by_freq) == 1:
        return 'YES'
    elif len(data_by_freq) == 2:
        len_1 = len(list(data_by_freq.values())[0])
        len_2 = len(list(data_by_freq.values())[1])
        freq_1 = list(data_by_freq.keys())[0]
        freq_2 = list(data_by_freq.keys())[1]
        if len_1 == 1 and (freq_1 - freq_2 == 1 or freq_1 == 1):
            return 'YES'
        elif len_2 == 1 and (freq_2 - freq_1 == 1 or freq_2 == 1):
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'


if __name__ == '__main__':
    # s = 'ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'
    # s = 'aaaabbcc'
    # s = 'abcdefghhgfedecba'
    s = 'aaaaabc'
    result = is_valid(s)
    print(result + '\n')
