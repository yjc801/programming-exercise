def evalRPN(tokens):
    if len(tokens) == 0:
        return None
    elif len(tokens) == 1:
        return int(tokens[0])

    stack = []
    stack.append(tokens.pop())
    while stack:
        c = tokens.pop()
        if isdigits(c) and isdigits(stack[-1]):
            num1 = int(c)
            num2 = int(stack.pop())
            op = stack.pop()
            if op == "+":
                res = num1 + num2
            elif op == "-":
                res = num1 - num2
            elif op == "*":
                res = num1 * num2
            elif op == "/":
                res = abs(num1)/abs(num2)
                if num1 * num2 < 0:
                    res = -res 
            tokens.append(str(res))
        else:
            stack.append(c)
    return tokens.pop()

def isdigits(c):
    if c.isdigit():
        return True
    elif len(c) > 1:
        if c[0] == "-" and c[1:].isdigit:
            return True
    else:
        return False

# s = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
s = ["1"]
print(isdigits("-11"))
print evalRPN(s)
            