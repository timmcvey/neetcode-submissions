class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # numFreq = defaultdict(int)
        # for num in nums:
        #     numFreq[num] += 1
        # remain = sorted(numFreq.items(), key=lambda x: x[1],reverse=True)[:k]
        # final = []
        # for k,v in remain:
        #     final.append(k)
        # return final

        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        frequency = [[] for i in range(len(nums)+1)]
        for num, count in count.items():
            frequency[count].append(num)
        # return frequency
        result = []

        for i in range(len(frequency)-1,0,-1):
            for num in frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result
