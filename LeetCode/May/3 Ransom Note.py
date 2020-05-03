class Solution:
    @staticmethod
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        n_dict = {letter: 0 for letter in ransomNote}

        for letter in ransomNote:
            start = magazine.find(letter, n_dict[letter]) + 1
            if start == 0: return False
            n_dict[letter] = start

        return True


if __name__ == '__main__':
    sentence = 'Red fox jumps over closure!'
    assert Solution.canConstruct('fox', sentence) is True
    assert Solution.canConstruct("a", "b") is False
    assert Solution.canConstruct("aa", "ab") is False
    assert Solution.canConstruct("aa", "aab") is True
    assert Solution.canConstruct("bjaajgea",
    "affhiiicabhbdchbidghccijjbfjfhjeddgggbajhidhjchiedhdibgeaecffbbbefiabjdhggihccec") is True
