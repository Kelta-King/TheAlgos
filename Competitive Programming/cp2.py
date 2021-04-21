import math

def squares(a, b):
    """
    sr = math.sqrt(a)
    count = 0
    while ((sr * sr) <= b):
        if ((sr * sr) >= a):
            count += 1
        sr += 1
    
    return count
    """
    x = a
    count = 0
    sqrs = []
    diff = 0
    while x <= b:
        
        if count == 0:
            rt = math.sqrt(x)
            if rt - int(rt) == 0:
                count += 1
                dnew = rt + 1
                dnew = 2*(dnew) - 1
                diff = dnew
                sqrs.append(x)
                x = x + dnew

            else:
                x += 1

        else:
            count += 1
            dnew = (diff) + 2
            diff = dnew
            sqrs.append(x)
            x = x + dnew
    
    return count

import time
begin = time.time()
print(squares(3, 80))
time.sleep(1)
end = time.time()
print(end-begin - 1)