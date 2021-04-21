
def queensAttack(n, k, r_q, c_q, obstacles):

    # Not obstracles
    if k == 0:

        up_cnt = n - r_q
        down_cnt = r_q - 1

        lft_cnt = c_q - 1
        rht_cnt = n - c_q

        ul_cnt = min(n - r_q, c_q - 1)
        ur_cnt = min(n - r_q, n - c_q)

        dl_cnt = min(r_q - 1, c_q - 1)
        dr_cnt = min(r_q - 1, n - c_q)

        return up_cnt + down_cnt + lft_cnt + rht_cnt + ul_cnt + ur_cnt + dl_cnt + dr_cnt

    else:
        
        minUL = min(n - r_q, c_q - 1)
        minUR = min(n - r_q, n - c_q)
        minDL = min(r_q - 1, c_q - 1)
        minDR = min(r_q - 1, n - c_q)
        minUP = n - r_q
        minDown = r_q - 1
        minRight = n - c_q
        minLeft = c_q - 1

        for obs in obstacles:

            if r_q == obs[0] and c_q > obs[1]:
                # Left
                minLeft = min(minLeft, c_q - obs[1] - 1)
                continue
            
            elif r_q == obs[0] and c_q < obs[1]:
                # Right
                minRight = min(minRight, obs[1] - c_q - 1)
                continue
            
            elif c_q == obs[1] and r_q > obs[0]:
                # Down
                minDown = min(minDown, r_q - obs[0] - 1)
            
            elif c_q == obs[1] and r_q < obs[0]:
                # Up
                minUP = min(minUP, obs[0] - r_q - 1)

            elif r_q < obs[0] and c_q > obs[1] and abs(r_q - obs[0]) == abs(c_q - obs[1]):
                # UpLeft
                minUL = min(minUL, abs(r_q - obs[0]) - 1)
                continue
            
            elif r_q < obs[0] and c_q < obs[1] and abs(r_q - obs[0]) == abs(c_q - obs[1]):
                # UpRight
                minUR = min(minUR, abs(r_q - obs[0]))
                continue
            
            elif r_q > obs[0] and c_q > obs[1] and abs(r_q - obs[0]) == abs(c_q - obs[1]):
                # DownLeft
                minDL = min(minDL, abs(r_q - obs[0]))
            
            elif r_q > obs[0] and c_q < obs[1] and abs(r_q - obs[0]) == abs(c_q - obs[1]):
                # DownRight
                minDR = min(minDR, abs(r_q - obs[0]))
            
            
        print("minUP: ",minUP)
        print("minDown: ",minDown)
        print("minRight: ",minRight)
        print("minLeft: ", minLeft)
        print("minUL: ", minUL)
        print("minUR: ", minUR)
        print("minDL: ", minDL)
        print("minDR: ", minDR)
        return minUP + minDown + minRight + minLeft + minUL + minUR + minDL + minDR

fptr = open('obstracles.txt', 'r')
obstacles = []

for x in fptr:
    z = x.split("\n")
    y = z[0].split(" ")
    y[0] = int(y[0])
    y[1] = int(y[1])
    obstacles.append(y)
n = 100
k = 100
r_q = 48
c_q = 81
print(queensAttack(n, k, r_q, c_q, obstacles))
