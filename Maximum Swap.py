class Solution(object):
    def maximumSwap(self, num):
        digits = list(str(num))
        last = {d: i for i, d in enumerate(digits)}
        for i, d in enumerate(digits):
            for larger in "9876543210":
                if larger <= d:
                    break
                if last.get(larger, -1) > i:
                    j = last[larger]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))
        return num