
def minimumDistances(a):
    
    minimum = []

    for i in range(len(a)):
        temp = i
        m = False
        for j in range(len(a)):
            if a[i] == a[j] and i != j:
                temp = abs(temp - j)
                m = True
            
        if m:
            minimum.append(temp)

    if len(minimum) > 0:
        return min(minimum)
    else:
        return -1

a = [7 ,1 ,3 ,4 ,1 ,7]
print(minimumDistances(a))
