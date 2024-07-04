class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        tmp = []
        for i in s:
            if i in brackets.values():
                tmp.append(i)
            else:
                if tmp and brackets[i]==tmp[-1]:
                    tmp.pop()
                else:
                    return True
            

        if tmp:
            return False
        return True