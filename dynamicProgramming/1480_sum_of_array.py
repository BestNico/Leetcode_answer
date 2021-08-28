from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """  
            [1, 2, 3, 4] => [1, 3, 6, 10]
            [1, 1, 1, 1, 1] => [1, 2, 3, 4, 5]
        """
        # dynamic programming
        # result = []
        # temp = 0

        # for i in nums:
        #     result.append(i+temp)
        #     temp += i
        
        # return result

        # new list
        newnums = nums
        for i in range(1,len(nums)):
            newnums[i] = newnums[i-1] + nums[i]
        return newnums



nums1 = [1,2,3,4]
nums2 = [1,1,1,1,1]
nums3 = [3,1,2,10,1]
s = Solution()
print(s.runningSum(nums1))
print(s.runningSum(nums2))
print(s.runningSum(nums3))