class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i,v in enumerate(nums):
            indices[v] = i

        for i,v in enumerate(nums):
            diff = target - v
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []