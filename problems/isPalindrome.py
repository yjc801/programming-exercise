def isPalindrome(x):
    if x < 0:
        return False
    d = 1
    while x/d >= 10:
        d*=10

    while x:
        quotient = x/d
        reminder = x % 10
        if quotient != reminder:
            return False
        x = x % d/10
        d /= 100
    return True

if __name__ == '__main__':
    print isPalindrome(121)