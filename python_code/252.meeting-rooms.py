class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        start_times = sorted([x[0] for x in intervals])
        end_times = sorted([x[1] for x in intervals])
        for i in range(len(start_times)-1):
            if end_times[i] > start_times[i+1]:
                return False
        return True