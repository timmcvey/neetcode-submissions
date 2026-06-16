class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSequence = 0
        for num in nums:
            sequenceLength = 1
            numPlusOne = num + 1
            while numPlusOne in nums:
                sequenceLength += 1
                numPlusOne += 1
            if sequenceLength > longestSequence:
                longestSequence = sequenceLength
        return longestSequence
                