class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648

        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend == MIN_INT:
                return MAX_INT
            return -dividend

        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        result = 0
        while divisor >= dividend:
            power_of_two = -1
            value = divisor
            while value >= MIN_INT and value + value >= dividend:
                value += value
                power_of_two += 1
            result += power_of_two
            dividend -= value

        return result if negatives == 1 else -result

s = Solution()
print(s.divide(10, 3))
# print(s.divide(7, -3))
# print(s.divide(0, 1))
# print(s.divide(1, 1))
print(s.divide(-1, -1))