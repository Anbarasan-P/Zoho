class climbing():
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        first = 1
        second = 2

        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third

        return second
    
# Example test case

TotalStairs = climbing()

print(f"Total Ways :", TotalStairs.climbStairs(2), "Ways")
print(f"Total Ways :", TotalStairs.climbStairs(7), "Ways")