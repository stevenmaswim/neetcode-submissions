"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        max_rooms = 0
        rooms = 0 
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)
        i = 0
        j = 0 
        while i < len(intervals):
            if starts[i] < ends[j]:
                i += 1
                rooms += 1 
            else: 
                j += 1

                rooms -= 1
            max_rooms = max(max_rooms, rooms)
        return max_rooms
            