from random import randint

def is_prime(n):
    a = randint(1, n - 1)
    print "1"
    b = a**(n-1)
    print "2"
    return b % n == 1

print "13", is_prime(13)
print "80", is_prime(80)
print "9851", is_prime(9851)
print is_prime(99999989)
