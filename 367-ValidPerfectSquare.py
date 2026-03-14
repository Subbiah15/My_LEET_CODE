class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        else:
            left=2
            right=num//2
            while left <= right:
                mid=(left+right)//2
                s=mid * mid
                if s==num:
                    return True
                elif s<num:
                    left=mid+1
                else:
                    right=mid-1
            return False
        
