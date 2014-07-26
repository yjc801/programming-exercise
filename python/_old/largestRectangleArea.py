def largestRectangleArea(height):
    res = 0
    stack = []
    height.append(0)
    i = 0
    while i < len(height):
        if not stack or height[i] > height[stack[-1]]:
            stack.append(i)
            i+=1
        else:
            tmp = stack.pop()
            width = i-stack[-1]-1 if stack else i
            print height[tmp]
            res = max(res,height[tmp]*width)
    return res

print largestRectangleArea([1,2,2])