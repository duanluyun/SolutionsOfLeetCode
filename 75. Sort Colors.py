class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start=0
        end=len(nums)-1
        mid=(start+end)//2
        for i in range(mid,-1,-1):
            self.sink(nums,i,end)
        for i in range(end,0,-1):
            nums[0],nums[i]=nums[i],nums[0]
            self.sink(nums,0,i-1)


    def sink(self,nums,start,end):
        root=start
        while True:
            child=2*root+1
            if child>end:
                break
            if child+1<=end and nums[child+1]>nums[child]:
                child+=1
            if nums[root]<nums[child]:
                nums[root],nums[child]=nums[child],nums[root]
                root=child
            else:
                break


