class Box:
    def getHeight(self, w, l, h, n):
        if n <= 0:
            return 0
         
        box = [(w[i], l[i], h[i]) for i in range(n)]
        box.sort(key = lambda b: (b[0], b[1]), reverse=True)
        height = [0] * n
         
        for i in range(n):
            height[i] = box[i][2]
            for j in range(i - 1, -1, -1):
                if box[j][0] > box[i][0] and box[j][1] > box[i][1]:
                    height[i] = max(height[i], height[j] + box[i][2])
        return max(height)
