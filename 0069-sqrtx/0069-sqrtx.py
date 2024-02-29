import math

class Solution:
    def mySqrt(self, x):
        square_root = math.sqrt(x)
        rounded = math.floor(square_root)
        return int(rounded)
        