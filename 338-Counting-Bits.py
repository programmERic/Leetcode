class Solution:
    def countBits(self, n: int):

        res = [0 for _ in range(n+1)]
        
        sb = 1
        for i in range(1, n+1):
            
            print(sb, i)

            if sb*2 == i:
                sb = i
                
            res[i] = 1 + res[i - sb]

        return res


v = Solution().countBits(n=65)
print(v)