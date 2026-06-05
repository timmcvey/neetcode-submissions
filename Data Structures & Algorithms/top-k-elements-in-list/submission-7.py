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

#2
        # count = defaultdict(int)

        # for num in nums:
        #     count[num] += 1

        # frequency = [[] for i in range(len(nums)+1)]
        # for num, count in count.items():
        #     frequency[count].append(num)
        # # return frequency
        # result = []

        # for i in range(len(frequency)-1,0,-1):
        #     for num in frequency[i]:
        #         result.append(num)
        #         if len(result) == k:
        #             return result

# 3
        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]

        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        # for num, cnt in count.items():
        #     freq[cnt].append(num)

        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for num in freq[i]:
        #         res.append(num)
        #         if len(res) == k:
        #             return res


# 4
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res        