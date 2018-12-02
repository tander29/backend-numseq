from numseq.fib import fib
from numseq.geo import square, triangle, cube
from numseq.prime import is_prime, primes
# can import * from numseq.geo or primes but
# creates a pep8 warning/bad practice for readability


print('Fibonacci')
for i in range(10):
    print('{}: {}'.format(i, fib(i)))

print
print
print('Geometric numbers')
for i in range(10):
    print('{}: {} {} {}'.format(i, square(i), triangle(i), cube(i)))

print
print
print('Primes')
prime_list = primes(1000)
for p in prime_list[-10:]:
    print p

print ("Is 999981 prime? {}".format(is_prime(999981)))
print ("Is 999983 prime? {}".format(is_prime(999983)))
