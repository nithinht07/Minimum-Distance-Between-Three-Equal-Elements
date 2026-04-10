from collections import defaultdict

class Solution:
    def minimumDistance(self, nums):
        pos = defaultdict(list)
        
        # Store indices for each value
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        ans = float('inf')
        
        # Check each value
        for indices in pos.values():
            if len(indices) < 3:
                continue
            
            # Try all triplets
            n = len(indices)
            for i in range(n):
                for k in range(i + 2, n):
                    dist = 2 * (indices[k] - indices[i])
                    ans = min(ans, dist)
        
        return ans if ans != float('inf') else -1