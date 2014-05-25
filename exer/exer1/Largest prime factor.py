__author__ = 'chy'
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

number = 600851475143
n=[]
i=1
while i < number:
    if number % i==0:
        number = number / i
        n.append(i)
        i += 1
print n