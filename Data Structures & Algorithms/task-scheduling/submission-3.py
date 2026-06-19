class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_to_freq = {}
        for task in tasks:
            if task not in task_to_freq:
                task_to_freq[task] = 1
            else:
                task_to_freq[task] += 1
        
        max_freq = -float('inf')
        max_task = None
        for task, freq in task_to_freq.items():
            if freq > max_freq:
                max_task = task
                max_freq = freq
        
        # Find all tasks with max freq
        num_max_tasks = 0
        for task, freq in task_to_freq.items():
            if freq == max_freq:
                num_max_tasks += 1
        
        return max((max_freq - 1)*(n + 1) + num_max_tasks, len(tasks))

