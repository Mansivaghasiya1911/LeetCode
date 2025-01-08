dividend = 7
divisor = -3
answer = 0
flag = 0
neg_divi = False
neg_divisor = False

if dividend< 0:
    neg_divi = True
    di = -(dividend)
else:
    di = dividend
if divisor<0:
    neg_divisor = True
    dis = -(divisor)
else:
    dis = divisor

if -2**31> dividend |  -2**31>divisor:
    print("hello")
    answer = -2**31
elif dividend > (2**31) -1 | divisor > (2**31) -1:
    answer = 2**31-1
else:
    while di>0:
        di -= dis
        flag+=1
    flag -=1
print(flag)

if neg_divisor and not neg_divi:
    answer = -(flag)
elif not neg_divisor and neg_divi:
    answer = -(flag)
else:
    answer = flag


def div_fun(x, y):
    if dividend < -2 ** 31 or divisor < -2 ** 31:
        return -2 ** 31
    elif dividend > (2 ** 31) - 1 or divisor > (2 ** 31) - 1:
        return 2 ** 31
    count = 0
    diff = abs(x)

    while diff >= abs(y):
        diff -= abs(y)
        count += 1

    if (x < 0) != (y < 0):
        count = -count

    return count

dividend = -2147483648
divisor = -1
div_fun(dividend, divisor)