class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        for i in text:
            if 'b' in text and 'a' in text and 'l' in text and 'o' in text and 'n' in text:
                numb = text.count('b')
                numa = text.count('a')
                numl = text.count('l')
                numo = text.count('o')
                numn = text.count('n')
                mins = min(numb,numa,numn,int(numl/2),int(numo/2))
                if mins*2 <= numl and mins*2 <= numo:
                    return mins
            return 0
