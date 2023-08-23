class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        m=math.prod(nums)
        if m>0:
            return 1
        return -1
