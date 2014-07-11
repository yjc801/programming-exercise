def intToRoman(num):
    table = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',\
    90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}

    i,d,res = 0,1000,""
    while num > 0:
        count = num/d
        num %= d
        while count > 0:
            if table.get(count):
                res+=table[count*d]
                break
            elif count > 5:
                res+=table[5*d]
                count-=5
            else:
                res+=table[d]
                count-=1
        d /= 10
    return res

if __name__ == '__main__':
    print intToRoman(3586)
    print intToRoman(5)
    print intToRoman(6)