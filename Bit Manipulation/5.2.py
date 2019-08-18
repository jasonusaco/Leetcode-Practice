"""
小数左移一位，如果实数大于1，说明小数点后一位是1，
如果小于1，说明小数点后一位是0
重复这个过程，即可得到实数的二进制表示
"""
class BinDecimal:
    def printBin(self, num):
        if num >= 1 or num <= 0:
            return "Error"

        binary = ['0', '.']

        while num > 0:
            if len(binary) >= 32:
                return "Error"

            r = num * 2
            if r >= 1:
                binary.append('1')
                num = r - 1
            else:
                binary.append('0')
                num = r
        return ''.join(binary)
        
