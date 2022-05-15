from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 常规思想
        """
        思路分析
            假并归
            控制两个指针 分别指向第一个列表和第二个列表
            移动条件：
                当A还未结束并且A指针所指值比B指针所指的值小或者B结束 -> 移动指针A
                否则移动指针B
            
        """
        m, n = len(nums1), len(nums2)
        lens = m + n
        left, right = -1, -1
        aStart, bStart = 0, 0

        for _ in range(lens//2 + 1):
            left = right
            if aStart < m and (bStart >= n or nums1[aStart] < nums2[bStart]):
                right = nums1[aStart]
                aStart += 1
            else :
                right = nums2[bStart]
                bStart += 1
        
        if (lens & 1) == 0:
            return (left + right) / 2.0
        
        return right


s = Solution()
nums1 = [1, 2, 3]
nums2 = [3, 4, 5, 6]

print(s.findMedianSortedArrays(nums1, nums2))
