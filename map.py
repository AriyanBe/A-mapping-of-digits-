class Solution(object):
    def letterCombinations(self, digits):
        self.digits = digits

    def mapping(self):
        maps = {
            1: '',
            2: ['a', 'b', 'c']
                }


def main():
    sol = Solution()
    
main()