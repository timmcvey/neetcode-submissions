class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = defaultdict(int)
        for num in nums:
            numFreq[num] += 1
        remain = sorted(numFreq.items(), key=lambda x: x[1],reverse=True)[:k]
        final = []
        for k,v in remain:
            final.append(k)
        return final


