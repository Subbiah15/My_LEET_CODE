class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        X=s[::-1]
        if s==X:
            return True
        else:
            return False
        
