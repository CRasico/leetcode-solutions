from typing import Dict

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        zagMap: Dict[int, str] = self.init_map(numRows)

        direction = True
        count = 0
        greaterThanOne = numRows > 1

        for character in s:
            zagMap[count] = zagMap[count] + character

            if direction is True:
                count += 1
            else:
                count -= 1

            if count == numRows:
                if greaterThanOne:
                    direction = not direction
                    count -= 2
            if count == 0:
                direction = not direction

        zagString = ""
        print(zagMap.values())
        for value in zagMap.values():
            zagString += value

        return zagString

    def init_map(self, numRows: int)-> Dict[int, str]:
        initMap: Dict[int, str] = {}
        for i in range(numRows):
            initMap[i] = ""
        return initMap

##############################################################
# The string "PAYPALISHIRING" is written 
# in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font 
# for better legibility)
#
# Take in a stirng X and a row count y and output the new
# string as it would output if read from left to right
#
#     PAYPALISHIRING -> PAHNAPLSIIGYIR
#
#     P   A   H   N
#     A P L S I I G
#     Y   I   R
#
##############################################################