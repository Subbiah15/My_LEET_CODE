import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        r = math.trunc(dividend/divisor)

        if r > 2**31 - 1:
            return 2**31 - 1
        elif r < -2**31:
            return -2**31
        
        return r
        
