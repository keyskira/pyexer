"""A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers."""
PalNum = []

def CheckPalNum(n):
    num = str(n)
    a = len(num)
    k = 0
    isPalNum = True
    while k < (a + 1) / 2:
        if num[k] == num[a - k - 1]:
            k = k + 1
        else:
            isPalNum = False
            break
    if isPalNum:
        if n not in PalNum:
            PalNum.append(n)


def GreatPalNum(m):
    def qsort(arr, left, right):
        key = arr[right]
        lp = left
        rp = right
        if lp == rp:
            return
        while True:
            while (arr[lp] >= key) and (rp > lp):
                lp = lp + 1
            while (arr[rp] <= key) and (rp > lp):
                rp = rp - 1
            arr[lp], arr[rp] = arr[rp], arr[lp]
            if lp >= rp:
                break
        arr[rp], arr[right] = arr[right], arr[rp]
        if left < lp:
            qsort(arr, left, lp - 1)
        qsort(arr, rp, right)

    qsort(m, 0, len(m) - 1)
    return m[0]


for i in range(100, 1000):
    for j in range(100, 1000):
        n = i * j
        CheckPalNum(n)

print GreatPalNum(PalNum)
