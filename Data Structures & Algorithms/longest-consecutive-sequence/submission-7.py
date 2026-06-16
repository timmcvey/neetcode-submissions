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
        # return longestSequence=
        nums.sort()
        lastNum = float('inf')
        longestSequence = 0
        currentSequence = 1
        for num in nums:
            if lastNum == num:
                continue
            if num + 1 in nums:
                currentSequence += 1
            else:
                longestSequence = max(longestSequence,currentSequence)    
                currentSequence = 1
            lastNum = num
        return longestSequence