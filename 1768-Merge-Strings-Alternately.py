class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged2 = []
        i,j = 0, 0
        while i<len(word1) or j<len(word2):
            if len(word1)>i:
                merged2.append(word1[i])
                i+=1
            if len(word2)>j:
                merged2.append(word2[j])
                j+=1
        return ''.join(merged2)
        