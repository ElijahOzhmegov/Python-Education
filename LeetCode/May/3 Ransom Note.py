class Solution:
    @staticmethod
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        m_dict = {letter: 0 for letter in set(magazine)}

        for letter in magazine:
            m_dict[letter] += 1

        for letter in ransomNote:
            if letter not in m_dict: return False
            m_dict[letter] -= 1
            if m_dict[letter] < 0: return False

        return True


if __name__ == '__main__':
    sentence = 'Red fox jumps over closure!'
    assert Solution.canConstruct('fox', sentence) is True
    assert Solution.canConstruct("a", "b") is False
    assert Solution.canConstruct("aa", "ab") is False
    assert Solution.canConstruct("aa", "aab") is True
    assert Solution.canConstruct("bjaajgea",
    "affhiiicabhbdchbidghccijjbfjfhjeddgggbajhidhjchiedhdibgeaecffbbbefiabjdhggihccec") is True
