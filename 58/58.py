# Num 58

class Solution(object):
    def lengthOfLastWord(self, s):
        if (len(s) > 0 ):
            if len([i for i in s.split(' ') if i != '']) > 0:
                return len([i for i in s.split(' ') if i != ''][-1])
        return 0
            

class Solution(object):
    def lengthOfLastWord(self, s):
        if not s:
            return 0
        s = s.strip(' ')
        L = s.split(' ')[-1]
        return len(L)
