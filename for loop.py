exp = [2200, 2400, 2600, 2800]
total = 0
for i in range (len(exp)):
    print("Months", i+1, "Exppense", exp[i])
    total = total + exp[i]
    print("Total expense is :", total)