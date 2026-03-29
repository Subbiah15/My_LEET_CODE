class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ad=int(a,2)
        bd=int(b,2)
        cd=ad+bd
        cb=bin(cd)
        return cb[2:]
        
