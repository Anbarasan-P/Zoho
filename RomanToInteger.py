class Solution:
    def romanToInt(self, s):
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0
        prev_value = 0

        for char in reversed(s):  # Start from the right end
            current_value = values[char]

            if current_value < prev_value:
                total -= (
                    current_value  # Subtract if smaller than the previous (right) value
                )
            else:
                total += current_value  # Otherwise, just add

            prev_value = current_value  # Update previous value for next loop

        return total


Roman = Solution()
print(Roman.romanToInt("III"))  # Output: 3
print(Roman.romanToInt("LVIII"))  # Output: 58
print(Roman.romanToInt("MCMXCIV"))  # Output: 1994
print(Roman.romanToInt("CIV"))