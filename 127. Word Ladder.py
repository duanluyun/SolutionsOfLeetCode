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
        wordList=set(wordList)

        char=[chr(i) for i in range(ord('a'),ord('z')+1)]

        res=[(beginWord,1)]
        while res:
            word,length=res.pop(0)
            if word==endWord:
                return length
            for i in range(len(word)):
                for c in char:
                    temp=word[:i]+c+word[i+1:]
                    if temp in wordList:
                        res.append((temp,length+1))
                        wordList.remove(temp)
        return 0



