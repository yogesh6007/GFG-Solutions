from bisect import bisect_right
class Solution:
    def findLongestWord(self, s: str, d: list) -> str:
        positions = [[] for _ in range(26)]
        for i, ch in enumerate(s):
            positions[ord(ch) - ord("a")].append(i)
        def isSubsequence(word):
            prev = -1
            for ch in word:
                arr = positions[ord(ch) - ord("a")]
                idx = bisect_right(arr, prev)
                if idx == len(arr):
                    return False
                prev = arr[idx]
            return True
        answer = ""
        for word in d:
            if isSubsequence(word):
                if len(word) > len(answer):
                    answer = word
                elif len(word) == len(answer) and word < answer:
                    answer = word
        return answer