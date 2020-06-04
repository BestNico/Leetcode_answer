class Solution(object):
    def numJewelsInStones(self, J, S):
        return sum([S.count(i) for i in J])

        


J = "aA"
S = "aAAbbbbb"

solution = Solution()
numb = solution.numJewelsInStones(J, S)
print(numb)