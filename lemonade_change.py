bills = [5,5,5,10,20]

bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
result = True
cash = {5:0, 10:0, 20:0}
for bill in bills:
    print("bill: ", bill)
    print("Cashh: ", cash)
    cash[bill] = cash[bill]+1

    if bill == 10:
        if cash[5] >= 1:
            cash[5] = cash[5]-1
        else:
            print("10****")
            result = False
            break;
    elif bill == 20:
        if cash[10] >= 1 and cash[5] >= 1:
            cash[5] = cash[5] - 1
            cash[10] = cash[10] - 1
        elif cash[5] >= 3 :
            cash[5] = cash[5] - 3
        else:
            print("20***")
            result = False
            break;
