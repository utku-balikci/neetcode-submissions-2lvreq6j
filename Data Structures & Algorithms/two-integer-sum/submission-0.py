class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        out={}

        for i, num in enumerate(nums):
            needed = target - num
            
            if needed in out:

                return [out[needed],i]

            out[num]=i


        