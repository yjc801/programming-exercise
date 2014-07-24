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

def intToRoman2(num):
    digit = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    symbol = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    res = ""
    while num:
        for i in xrange(len(digit)):
            if digit[i] <= num:
                num-=digit[i]
                res+=symbol[i]
                break
    return res

if __name__ == '__main__':
    print intToRoman(3586)
    print intToRoman2(3586)
    print intToRoman(5)
    print intToRoman(6)