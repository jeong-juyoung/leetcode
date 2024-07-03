class Solution:
    def removeStars(self, s: str) -> str:
        tmp = []
        for i in s:
            if i == '*':
                tmp.pop(-1)
            else: 
                tmp.append(i)
        return "".join(tmp)