from collections import defaultdict

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

def maxPoints(points):
    if len(points) <= 2:
        return len(points)
    slops = []
    # d = defaultdict(int)
    d = dict()
    for index, curr in enumerate(points):
        for next in points[index+1:]:
            try:
                slop = 1.0*(curr.y-next.y)/(curr.x-next.x)
                intercept = curr.y - slop*curr.x
            except:
                slop = curr.x
                intercept = 0
            # d[(slop,intercept)]+=1
            try:
                d[(slop,intercept)]+=1
            except KeyError:
                d[(slop,intercept)]=1
    print d
    return max(d.values())

if __name__ == '__main__':
    print maxPoints([Point(1,1),Point(1,1),Point(2,3)])