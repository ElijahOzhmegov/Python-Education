class Solution:
    @staticmethod
    def findComplement(num: int) -> int:
        res = int(''.join(['0' if f == '1' else '1' for f in format(num, 'b')]), 2)
        return res


if __name__ == '__main__':
    assert 2 == Solution.findComplement(5)
    assert 0 == Solution.findComplement(1)

