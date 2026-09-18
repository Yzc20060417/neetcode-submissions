class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for i in s:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1
        for j in t:
            if j not in map:
                return False
            else:
                map[j] -= 1
        for v in map.values():
            if v != 0:
                return False
        return True
        