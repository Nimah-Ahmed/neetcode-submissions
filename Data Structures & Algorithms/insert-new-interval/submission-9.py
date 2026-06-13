class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # ITERATIVE SOLUTION --> O(n) time

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
            
        
        # Initialization
        currentInterval = None
        intervalToInsert = []
        output = []

        # Maintenance
        for i in range(len(intervals)):
            currentInterval = intervals[i]
            if overlaps(currentInterval, newInterval):
                if intervalToInsert == []:
                    intervalToInsert = [float('inf'), float('inf')]
                    intervalToInsert[0] = min(currentInterval[0], newInterval[0])
                    intervalToInsert[1] = max(currentInterval[1], newInterval[1])
                else:
                    intervalToInsert[0] = min(currentInterval[0], newInterval[0], intervalToInsert[0])
                    intervalToInsert[1] = max(currentInterval[1], newInterval[1], intervalToInsert[1])
            else:
                if intervalToInsert == []:
                    output.append(currentInterval)
                else:
                    output.append(intervalToInsert)
                    output.append(currentInterval)
                    intervalToInsert = []
        
        if intervalToInsert != []:
            output.append(intervalToInsert)
        if intervals == []:
            output.append(newInterval)
        
        # Insert newInterval if you have not yet
        if newInterval[1] < output[0][0]:
            output.insert(0, newInterval)
        for i in range(len(output) - 1):
            if output[i][1] < newInterval[0] < output[i+1][0]:
                output.insert(i + 1, newInterval)
        if newInterval[0] > output[-1][1]:
            output.append(newInterval)
        return output
                