import re
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        charList=[]
        for i in s:
            if re.match('[a-zA-Z0-9]',i):
                charList.append(i.lower())
        return charList==charList[::-1]



