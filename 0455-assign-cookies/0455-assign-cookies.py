class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()

        child_i = 0
        cookie_j = 0
        content_children = 0


        while child_i < len(g) and cookie_j < len(s):
            # cookie 가 child 보다 크거나 같으면 
            print(f"child_i : {s[cookie_j]}")
            print(f"cookie_j : {g[child_i]}")
            if s[cookie_j] >= g[child_i]:
                content_children += 1
                child_i += 1
            cookie_j += 1
        return content_children