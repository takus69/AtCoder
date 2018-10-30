def gcd(x, y):
    '''ユークリッド互除法'''
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return gcd(y, x % y)
 

if __name__ == '__main__':
    msg = 'test for gcd'
    assert gcd(5, 3)==1, msg
    assert gcd(12, 4)==4, msg
