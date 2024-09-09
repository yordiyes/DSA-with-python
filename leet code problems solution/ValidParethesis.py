class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        val = True
        for i in range(len(s)-1):
        	if len(s) == 1:
                val = False
            elif s[i] == "[":
            	if s[i+1] != "]":
                    val = False
                else:
                    val = True
            elif s[i] == "(":
                if s[i+1] != ")":
                    val = False
                else:
                    val = True
            elif s[i] == "{":
                if s[i+1] != "}":
                    val = False
                else:
                    val = True        
            else:
                pass
        return val

solution = Solution()
result = solution.isValid("[")
print(result)