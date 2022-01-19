from typing import List

class Solution: 
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        elif len(stones) == 0:
            return None

        stones.sort(reverse = True)
        stoneX = stones.pop(0)
        stoneY = stones.pop(1)

        newStone = abs(stoneX - stoneY)
        if newStone > 0:
            stones.append(newStone)
        return self.lastStoneWeight(stones)
