class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for key,val in count.items():
            buckets[val].append(key)
        res = []
        for f in range(len(nums),0,-1):
            for x in buckets[f]:
                res.append(x)
                if len(res) == k:
                    return res        
            