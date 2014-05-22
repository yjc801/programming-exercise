def longestConsecutive(num):
    if not num:
        return 0
    hash_table = set()
    for value in num:
        hash_table.add(value)

    max_length = 0
    for value in num:
        counter = 1
        temp = value
        while 1:
            temp += 1
            if temp in hash_table:
                hash_table.remove(temp)
                counter += 1
            else:
                break
        temp = value
        while 1:
            temp -= 1
            if temp in hash_table:
                hash_table.remove(temp)
                counter += 1
            else:
                break
        max_length = max(max_length,counter)
    return max_length


if __name__ == '__main__':
    A = [0]
    print longestConsecutive(A)