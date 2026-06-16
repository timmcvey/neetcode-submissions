class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # longestSequence = 0
        # for num in nums:
        #     sequenceLength = 1
        #     numPlusOne = num + 1
        #     while numPlusOne in nums:
        #         sequenceLength += 1
        #         numPlusOne += 1
        #     if sequenceLength > longestSequence:
        #         longestSequence = sequenceLength
        # return longestSequence

        # solution2
        # nums.sort()
        # lastNum = float('inf')
        # longestSequence = 0
        # currentSequence = 1
        # for num in nums:
        #     if lastNum == num:
        #         continue
        #     if num + 1 in nums:
        #         currentSequence += 1
        #     else:
        #         longestSequence = max(longestSequence,currentSequence)    
        #         currentSequence = 1
        #     lastNum = num
        # return longestSequence

    # solution3
            # numSet = set(nums)
            # longest = 0

            # for num in numSet:
            #     if (num - 1) not in numSet:
            #         length = 1
            #         while (num + length) in numSet:
            #             length += 1
            #         longest = max(length, longest)
            # return longest

# solution4
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res            # 