def maxArea(height):
    res = -float('inf')
    area = 0
    low,high = 0,len(height)-1
    while low < high:
        area = min(height[low],height[high])*(high-low)
        res = max(res,area)
        if height[low] <height[high]:
            low+=1
        else:
            high-=1
    return res