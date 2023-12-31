# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
 
# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

#  Constraints:
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

from ast import List

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) == 1: return intervals

    intervals.sort(key=lambda x : x[0])

    i = 0
    result = []

    while i < len(intervals) - 1:
        first = intervals[i]
        second = intervals[i + 1]

        if first[1] >= second[0]:
            endTime = max(first[1], second[1])
            result.append([first[0], endTime])
            i += 1
        else:
            result.append(first)
            if (i + 1) == (len(intervals) - 1):
                result.append(second)
            i += 1

        return result
