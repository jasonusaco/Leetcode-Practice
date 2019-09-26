class Solution:
    def floodFill(self, image, sr, sc, newColor):
        R=len(image)
        C=len(image[0])
         
        oldColor=image[sr][sc]
        if oldColor==newColor:
            return image
        def dfs(r,c):
            if image[r][c]==oldColor:
                image[r][c]=newColor
                if r>=1:
                    dfs(r-1,c)
                if r<R-1:
                    dfs(r+1,c)
                if c>=1:
                    dfs(r,c-1)
                if c<C-1:
                    dfs(r,c+1)
        dfs(sr,sc)
        return image
