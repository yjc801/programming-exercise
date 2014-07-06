class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def insert(intervals, newInterval):
    count = 0
    while count < len(intervals):
        if newInterval.end < intervals[count].start:
            intervals.insert(count,newInterval)
            return intervals
        elif newInterval.start > intervals[count].end:
            count+=1
            continue
        else:
            newInterval.start = min(newInterval.start,intervals[count].start)
            newInterval.end = max(newInterval.end,intervals[count].end)
            del intervals[count]
    intervals.append(newInterval)
    return intervals


if __name__ == '__main__':
    new = insert([Interval(1,3),Interval(6,9)],Interval(2,5))
    print [[s.start,s.end] for s in new]