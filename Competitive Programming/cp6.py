
def compare(t1, t2):

    res = 0
    for i,j in zip(t1, t2):

        if int(i) or int(j):
            res += 1
    
    return res

def acmTeam(topic):

    m = 0
    cnt = 0
    
    for i in range(len(topic)):

        for j in range(i+1, len(topic)):

            res = 0
            for x,y in zip(topic[i], topic[j]):

                if int(x) or int(y):
                    res += 1
            if res > m:
                m = res
                cnt = 1
            elif res == m:
                cnt += 1

    res = [m, cnt]

    return res

#print(compare('10101', '11100'))
print(acmTeam(['10101', '11100', '11010', '00101']))