class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums==None or len(nums)<1:
            return None
        start=0
        end=len(nums)-1
        middle=(start+end)//2
        root=TreeNode(nums[middle])
        root.left=self.sortedArrayToBST(nums[:middle])
        root.right=self.sortedArrayToBST(nums[middle+1:])
        return root
