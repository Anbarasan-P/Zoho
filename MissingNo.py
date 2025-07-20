class Number():
    def Missingno(self, nums):
        n = len(nums)
        total = n * (n+1)//2
        return total - sum(nums)
    
solutionNumber = Number()



print(solutionNumber.Missingno([9,6,4,2,3,5,7,0,1]))