class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # ITERATIVE SOLUTION

        # Overlap checker
        def overlaps(interval_1, interval_2):
            if interval_2[0] <= interval_1[0] <= interval_2[1]:
                return True
            if interval_2[0] <= interval_1[1] <= interval_2[1]:
                return True
            if interval_1[0] <= interval_2[0] <= interval_1[1]:
                return True
            if interval_1[0] <= interval_2[1] <= interval_1[1]:
                return True
            return False

        # Sort intervals according to start time
        intervals.sort(key = lambda x: x[0])

        # Create output
        output = [intervals[0].copy()]
        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            if overlaps(current_interval, output[-1]):
                output[-1][0] = min(output[-1][0], current_interval[0])
                output[-1][1] = max(output[-1][1], current_interval[1])
            else:
                output.append(current_interval)
        return output
            