class Solution(object):
    def numberOfSteps(self, num):
        return num.bit_length() + bin(num).count('1') - 1

num = 9
s = Solution()
print(s.numberOfSteps(num))