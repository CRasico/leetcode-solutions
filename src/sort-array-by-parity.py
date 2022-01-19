from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_map = {}
        odd_map = {}

        for index in range(len(nums)):
            current = nums[index]
            if index % 2 == 0: 
                if current % 2 != 0:
                    if len(even_map) > 0: 
                        key = list(even_map.keys())[0]
                        value = even_map.pop(key)
                        nums[index] = value
                        nums[key] = current
                    else:
                        odd_map[index] = current
            else:
                if current % 2 != 1:
                    if len(odd_map) > 0: 
                        key = list(odd_map.keys())[0]
                        value = odd_map.pop(key)
                        nums[index] = value
                        nums[key] = current
                    else:
                        even_map[index] = current
        return nums


# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
# Return any answer array that satisfies this condition.

# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
# Sample Run:
# 0,4 even index, even number
# 1,2 odd index, even number (STORE!)
# 2,5 even index, odd number (SWAP WITH STORE!)
# 3, 7 odd index, odd number (DONE)