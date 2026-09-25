class Solution:
    def maxHeight(self, height: list[int], width: list[int], length: list[int]) -> int:
        boxes = []
        for i in range(len(height)):
            h, w, l = height[i], width[i], length[i]
            a, b = sorted((w, l))
            boxes.append((a, b, h))
            a, b = sorted((h, l))
            boxes.append((a, b, w))
            a, b = sorted((h, w))
            boxes.append((a, b, l))
        boxes.sort(key=lambda x: x[0] * x[1])
        n = len(boxes)
        dp = [0] * n
        for i in range(n):
            dp[i] = boxes[i][2]
            for j in range(i):
                if boxes[j][0] < boxes[i][0] and boxes[j][1] < boxes[i][1]:
                    dp[i] = max(dp[i], dp[j] + boxes[i][2])
        return max(dp)