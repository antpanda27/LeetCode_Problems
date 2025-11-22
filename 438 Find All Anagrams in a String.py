class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter(p)
        i = 0
        ans = []
        for j in range(len(s)):
            count[s[j]] -= 1
            while count[s[j]] < 0:
                count[s[i]] += 1
                i += 1
            if j - i + 1 == len(p):
                ans.append(i)
        return ans