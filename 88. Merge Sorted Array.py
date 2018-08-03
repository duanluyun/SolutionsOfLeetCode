class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 or n > 0:
            if m > 0 and n > 0:
                nums1[m + n - 1] = max(nums1[m - 1], nums2[n - 1])
                if nums1[m - 1] > nums2[n - 1]:
                    m -= 1
                else:
                    n -= 1
            elif m == 0:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            elif n == 0:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1





