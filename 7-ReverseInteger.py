class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x=abs(x)
        r=int(str(x)[::-1])
        r=r*sign
        if (-2**31 >r) or (r > 2**31 -1):
            return 0
        
        return r
