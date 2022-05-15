from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 暴力双循环
        # results: List[int] = []
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             results.extend([i, j])
        
        # return results
        
        # 优化解法 map寻值法
        tmp_dic = {}
        for i in range(len(nums)):
            if (t := target - nums[i]) in tmp_dic.keys():
                return [tmp_dic.get(t), i]
            else:
                tmp_dic[nums[i]] = i

        return []

s = Solution()
nums = [3, 2, 4, 5]
target = 6
print(s.twoSum(nums, target))