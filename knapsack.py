def fractional_knapsack(value, weight, capacity):
    """Return maximum value of items and their fractional amounts.

    (max_value, fractions) is returned where max_value is the maximum value of
    items with total weight not more than capacity.
    fractions is a list where fractions[i] is the fraction that should be taken
    of item i, where 0 <= i < total number of items.

    value[i] is the value of item i and weight[i] is the weight of item i
    for 0 <= i < n where n is the number of items.

    capacity is the maximum weight.
    """
    # index = [0, 1, 2, ..., n - 1] for n items
    index = list(range(len(value)))
    m = index.copy()
    # contains ratios of values to weight
    ratio = [v / w for v, w in zip(value, weight)]
    # index is sorted according to value-to-weight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)
    # print(ratio)
    mi=[x+1 for x in index]
    val = []
    wi =[]
    rat = []
    xi = []
    mx = []
    cap = []
    # u = u -wixi
    pixi = []
    wixi = []
    max_value = 0
    fractions = [0] * len(value)
    for i in index:
        #print(m[i],value[i],weight[i],ratio[i],fractions[i])


        if weight[i] <= capacity:
            cap.append(capacity)
            cap.append("-")
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
            # mi.append(m[i])
            val.append(value[i])
            wi.append(weight[i])
            rat.append(ratio[i])
            xi.append(fractions[i])
            cap.append(weight[i])
            cap.append("=")
            cap.append(capacity)
            pixi.append(value[i] * fractions[i])
            wixi.append(weight[i] * fractions[i])
        else:
            cap.append(capacity)
            cap.append("-")
            fractions[i] = capacity / weight[i]
            max_value += value[i] * capacity / weight[i]
            # mi.append(m[i])
            val.append(value[i])
            wi.append(weight[i])
            rat.append(ratio[i])
            xi.append(fractions[i])
            xi.append(0)

            cap.append(weight[i])
            cap.append("*")
            cap.append(fractions[i])
            cap.append("=")
            cap.append(0)
            pixi.append(value[i] * fractions[i])
            pixi.append(0)
            wixi.append(weight[i] * fractions[i])
            wixi.append(0)
            break
    uiwi = ""
    for i in cap:
        uiwi += str(i)
    print("Object i :",mi)
    print("Pi :",val)
    print("Wi :",wi)
    print("Pi/Wi :",rat)
    print("Xi :",xi)
    print("U - WiXi :",uiwi)
    print("PiXi :",pixi)
    print("WiXi :",wixi)
    tot_weight = sum(wixi)


    return max_value, fractions,tot_weight


n = int(input('Enter number of items: '))
value = input('Enter the values of the {} item(s) in order: '
              .format(n)).split()
value = [int(v) for v in value]
weight = input('Enter the positive weights of the {} item(s) in order: '
               .format(n)).split()
weight = [int(w) for w in weight]
capacity = int(input('Enter maximum weight: '))

max_value, fractions ,tot_weight = fractional_knapsack(value, weight, capacity)
print('The optimal solution x1,...xn that gives maximum profit is :', fractions)
print('The total profit is : ΣPiXi is', max_value)
print('The total weight is ΣWiXi  is ',tot_weight)


