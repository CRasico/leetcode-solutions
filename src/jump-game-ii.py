"""
Notes:
  - What do we know:
    - We can jump nums[i] distance with our next move if we want to 
    - This means our next jump can be at any of the spots within nums[i] in the list
    - Example: nums[i] == 2 we can jump to spot i + 1 or i + 2 just depends on what we want to do 
    - We don't know all of the contents of the list at the begging so the best way is to calculate the next jump in the list
    
Solution:
  - We should be able to recursively take our jumps throughout the list persisting the index we are at
  - Continue counting the index every time we take a jump
  - The solution will take a depth first search approach as we will always guess with the lowest value fist (this could be detrimental to the algorithm, but we could fix with memo)
  
  - Base case: 
    - Whether or not our current index is greater than the length of the board
  
  - Action:
    - For each value in range I recursively check what happens at the next index 
    
  - Result:
    - Return our minimum count we calculated at each node
"""
import sys

class Solution(object):
    def __init__(self):
        self.memory = {}

    def jumpRecursive(self, nums, index = 0):
        if index >= len(nums) - 1:
          return 0

        if index in self.memory:
            return self.memory[index]
        
        result = sys.maxsize  # current horrible result
        jumpLength = nums[index]
        for i in range(index + 1, index + jumpLength + 1):
            result = min(result, 1 + self.jumpRecursive(nums, i))

        self.memory[index] = result
        return result
  
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.memory = {}
        return self.jumpRecursive(nums, 0)
        