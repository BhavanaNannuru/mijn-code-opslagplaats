class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1        
        nums[j:]=[0]*(len(nums)-j)

