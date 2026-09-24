class Solution:
    def maxStackHeight(self, r, h):
        discs = sorted(zip(r, h))
        vals = sorted(set(h))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        bit = [0] * (len(vals) + 1)
        ans = 0
        i = 0
        n = len(discs)
        while i < n:
            j = i
            while j < n and discs[j][0] == discs[i][0]:
                j += 1
            updates = []
            for k in range(i, j):
                height = discs[k][1]
                x = rank[height] - 1
                best = 0
                while x:
                    best = max(best, bit[x])
                    x -= x & -x
                total = best + height
                updates.append((rank[height], total))
                ans = max(ans, total)
            for x, total in updates:
                while x <= len(vals):
                    bit[x] = max(bit[x], total)
                    x += x & -x
            i = j
        return ans