class Solution(object):
    def reverseString(self,s):
        return s[::-1]
    
string = "hello"
solution = Solution()
print(solution.reverseString(string))