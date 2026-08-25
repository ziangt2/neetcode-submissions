from collections import Counter
from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        task = count.values()
        task = [-x for x in task]
        heapq.heapify(task)
        time = 0
        q = deque()
        while task or q:
            time += 1
            if q and q[0][1] == time:
                heapq.heappush(task,q[0][0])
                q.popleft()
            if task:
                cnt = heapq.heappop(task)
                cnt += 1
         
                if cnt< 0:
                    q.append((cnt, time + n +1))
  
        return time