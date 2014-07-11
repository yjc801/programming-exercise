def merge(intervals):
    if not intervals:
        return []
    res = []
    for interval in intervals:
        res = insert(res,interval)
    return res

def insert(intervals,new):
    count = 0
    while count < len(intervals):
        if new.end < intervals[count].start:
            intervals.insert(count,new)
            return intervals
        elif new.start > intervals[count].end:
            count+=1
            continue
        else:
            new.start = min(new.start,intervals[count].start)
            new.end = max(new.end,intervals[count].end)
            del intervals[count]
    intervals.insert(count,new)
    return intervals