class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        j = 0
        for i in nums:   
            if target - i in seen:
                return [seen[target - i], j]
            seen[i] = j
            j += 1
        