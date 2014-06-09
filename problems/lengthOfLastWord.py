def lengthOfLastWord(s):
    res = s.strip().split()
    return len(res[-1]) if res else 0


if __name__ == '__main__':
	print lengthOfLastWord(" ")
	print lengthOfLastWord("a ")
	print lengthOfLastWord("a bc")