
def taumBday(b, w, bc, wc, z):
    # Write your code here
    b1 = b*bc
    b2 = b*(wc + z)

    w1 = w*wc
    w2 = w*(bc + z)

    return min(b1, b2) + min(w1, w2)

print(taumBday(3, 6, 9, 1, 1))