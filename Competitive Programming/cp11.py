
def biggerIsGreater(w):
    
    w = list(w)
    i = len(w) - 1

    while i > 0 and w[i-1] >= w[i]:
        i -= 1
    
    if i <= 0:
        return "no answer"

    j = len(w) - 1
    while (w[i-1] >= w[j]):
        j -= 1

    w[i-1], w[j] = w[j], w[i-1]
    w[i:] = w[len(w)-1:i-1:-1]

    return ''.join(w)


w = ['lmno', 'dcba', 'dcbb', 'abdc', 'abcd', 'fedcbabcd']

for x in w:
    print(biggerIsGreater(x))
