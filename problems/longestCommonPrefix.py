def longestCommonPrefix(strs):
    if not strs:
        return ""
    first = strs[0]
    for key, char in enumerate(first):
        for string in strs:
            if key > len(string)-1  or char != string[key]:
                return first[:key]
    return first

if __name__ == '__main__':
	print longestCommonPrefix(["aa","ab"])