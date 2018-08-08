class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        charList=[chr(i) for i in range(ord('a'),ord('z')+1)]
        req=[(beginWord,1)]
        while req:
            begin,length=req.pop(0)
            for i in range(len(begin)):
                for c in charList:
                    temp=begin[:i]+c+begin[i+1:]
                    if temp==endWord:
                        return length+1
                    if temp in wordList:
                        req.append((temp,length+1))
                        wordList.remove(temp)


S=Solution()
print(S.ladderLength('hit','cog', ["hot","dot","dog","lot","log","cog"]))



