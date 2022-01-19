from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}
        for item in strs:
            hash_total = 0
            for character in item:
                hash_total += hash(character)
            if hash_total in anagrams_dict:
                temp = anagrams_dict[hash_total]
                temp.append(item)
                anagrams_dict[hash_total] = temp
                continue
            anagrams_dict[hash_total] = [item]

        return anagrams_dict.values() 