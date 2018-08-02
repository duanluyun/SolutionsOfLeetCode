class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res=[]
        for token in path.split('/'):
            if token=='' or token=='.':
                continue
            elif token=='..':
                if res:
                    res.pop()
            else:
                res.append(token)
        return '/'+'/'.join(res)

S=Solution()
print(S.simplifyPath("/a/./b/../../c/"))

