class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        results = []
        low = lower - 1
        nums.append(upper + 1)
        for num in nums:
            diff = num - low
            if diff == 2:
                results.append(str(low+1))
            elif diff > 2:
                results.append(str(low+1) + "->" + str(num-1))
            low = num
        return results
