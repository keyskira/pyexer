# coding=utf-8
"""寻找600851475143的最大质因数"""
n = 600851475143
primes = [2]
i = 1
prime = n
while i < n:  #从i算到n
    for j in primes:
        if i % j == 0:  #查看i是不是已知质因数的倍数，如果是就忽略
            i = i + 1
        elif n % i == 0:
            n = n / i
            primes.append(i)  #把n的质因数存入primes
            i = i + 1
        else:
            i = i + 1
primes.remove(2)  #2是primes初值，并不一定是n的质因数，故去除
                  #此时primes里面是除了最大质因数外的其他质因数（为什么？我没搞懂，我感觉应该是已经包括最大质因数了）
for k in primes:
    prime = prime / k  #把n除以所有的除了最大的质因数以外的质因数，剩下的就是最大的质因数
print prime
