"""
Lothar Collatz hypothesis, 1937
"""
def LotharCollatz(c0):
    if c0 <= 0:
        return "Cannot use this number for the hypotesys"
    else:
        step = 0
        while c0 != 1:
            if c0 % 2 == 0:
                c0 = c0 / 2
            elif c0 % 2 == 1:
                c0 =  3 * c0 + 1
            step += 1
        return step

c0 = int(input("Enter a number: "))
print(LotharCollatz(c0))

