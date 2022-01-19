from typing import List
class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        map_seen = {}
        for item in arr:
            if item in map_seen:
                map_seen[item] += 1
                continue
            map_seen[item] = 1
        
        for key, value in reversed(map_seen.items()):
            if (key - 1) in map_seen:
                count += map_seen[key - 1]

        return count

             
            