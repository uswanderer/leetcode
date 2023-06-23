# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1

from ast import List

def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    usedRooms = 0

    if not intervals:
        return usedRooms
    
    startTimes = sorted([i[0] for i in intervals])
    endTimes = sorted(i[1] for i in intervals)
    length = len(intervals)
    endIdx = 0
    startIdx = 0

    while startIdx < length:
        if startTimes[startIdx] >= endTimes[endIdx]:
            usedRooms -= 1
            endIdx += 1
        
        usedRooms += 1
        startIdx += 1

    return usedRooms