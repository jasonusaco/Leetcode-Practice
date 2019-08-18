class CatDogAsylum:
    def asylum(self, ope):
        s = []
        res = []
        for v in ope:
            if v[0] == 1:
                s.append(v[1])
            else:
                if v[1] == 0 and s:
                    res.append(s.pop(0))
                else:
                    for i, si in enumerate(s):
                        if v[1] * si > 0:
                            res.append(s.pop(i))
                            break
        return res
