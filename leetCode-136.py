class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            contador = 0
            for otro in nums:
                if num == otro:
                    contador += 1
            if contador == 1:
                return num
            
solucion = Solution()

print(solucion.singleNumber([2,2,3]))
print(solucion.singleNumber([4,1,2,1,2]))
print(solucion.singleNumber([1]))
