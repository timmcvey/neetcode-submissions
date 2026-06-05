class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        compnums = set()
        for num in nums:
            if num in compnums:
                return True
            else:
                compnums.add(num)
        return False