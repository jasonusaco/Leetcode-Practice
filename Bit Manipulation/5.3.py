class CloseNumber:
    def getCloseNumber(self, x):
        res = [0,0]
        n = x
        while True:
            n -= 1
            if bin(x).count("1") == bin(n).count("1"):
                res[0] = n
                break
        n = x
        while True:
            n += 1
            if bin(x).count("1") == bin(n).count("1"):
                res[1] = n
                break
        return res
