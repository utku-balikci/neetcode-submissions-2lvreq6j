class Solution:
    def topKFrequent(self, nums, k):
        countMap = {}
        result = []

        # count frequency
        for num in nums:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1

        # find top k
        for _ in range(k):
            maxCount = 0
            mostFrequent = None

            for num in countMap:
                if countMap[num] > maxCount:
                    maxCount = countMap[num]
                    mostFrequent = num

            result.append(mostFrequent)
            del countMap[mostFrequent]

        return result