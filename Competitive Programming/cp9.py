def kaprekarNumbers(p, q):
    
    numbers = []
    for i in range(p,q+1):
        
        temp = i**2
        addition = 0
        dcount = 0
        
        for digit in str(temp):
            addition += int(digit)
            dcount += 1
        
        iLen = len(str(i))    
        x = str(temp)
        y = str(temp)
        r = int(x[dcount-iLen:])
        #print(x)
        #print(r)
        if y[:dcount-iLen] == '':
            l = 0
        else:
            l = int(y[:dcount-iLen])
        
        if r + l == i:
            numbers.append(i)
        
    
    if len(numbers) > 0:
        return numbers
    else:
        return "INVALID RANGE"

p = 400
q = 700
x = kaprekarNumbers(p, q)
val = ''
for i in x:
    val += str(i) + ' '
    
print(val)
