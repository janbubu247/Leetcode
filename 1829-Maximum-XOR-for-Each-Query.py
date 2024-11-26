class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        xorSum = 0
        maxXor = (1<<maximumBit)-1
        for i in nums:
            xorSum^=i
        answer = []
        for i in range(len(nums)):
            answer.append(maxXor^xorSum)
            xorSum^=nums.pop()
        return answer