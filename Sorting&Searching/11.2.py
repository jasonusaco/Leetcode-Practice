class SortString:
    def sortStrings(self, s, n):
        s = ["ab","ba","abc","cba"]
        temp = {}
        for si in s:
            k = ''.join(sorted(si))
            print(k)
            if k in temp:
               temp[k] = min(temp[k], si)
            else:
                temp[k] = si
        return sorted(list(temp.values()))
