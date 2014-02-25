def isValid(s):
	stack = list()
	open_brackets= set(["{","(","["])
	close_brackets = set(["}",")","]"])
	for i in s:
		if i in open_brackets:
			stack.append(i)
		elif i in close_brackets:
			try:
				tmp = stack[-1]
			except IndexError:
				return False
			if (i == "(" and tmp == ")") or (i == "{" and tmp == "}") or (i == "[" and tmp == "]"):
				stack.pop()
			else:
				return False

	if stack:
		return False
	else:
		return True

if __name__ == '__main__':
	s = "s(s]dd)"
	print isValid(s)