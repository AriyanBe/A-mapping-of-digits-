class Solution(object):
    def letterCombinations(self, digits):
        self.digits = digits
        combinations = []
        if digits:
            self.generate_combinations(0, '', combinations)
        return combinations

    def mapping(self, digit):
        maps = {
            0: '',
            1: '',
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }
        return maps[digit]

    def generate_combinations(self, index, current, combinations):
        if index == len(self.digits):
            combinations.append(current)
            return

        digit = int(self.digits[index])
        letters = self.mapping(digit)

        for letter in letters:
            self.generate_combinations(index + 1, current + letter, combinations)


def main():
    sol = Solution()
    digits = ""  # An empty string
    result = sol.letterCombinations(digits)
    print(result)


main()