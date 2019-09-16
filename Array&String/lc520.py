class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word:
            return True
        if word.lower() == word:
            return True
        for i in range(0,len(word)):
            if word[0].upper() == word[0] and word[1:].lower() == word[1:]:
                return True
        else:
            return False
