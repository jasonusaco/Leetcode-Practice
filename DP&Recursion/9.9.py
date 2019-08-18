class Queens:
    def nQueens(self, n):
        self.count = 0
        self.a = [0 for i in range(n+1)]
        self.Queens1(1,n)
        return self.count

    def Queens1(self,i,n):
        if i > n:
            self.count += 1
            return
        for j in range(i, n+1):
            self.a[j] = j
            if self.Place(i):
                self.Queens1(i+1, n)

    def Place(self, i):
        for j in range(1, i):
            if self.a[j]==self.a[i] or self.a[j]-self.a[i]==j-i or self.a[j]-self.a[i]==i-j:
                return 0
            return 1
