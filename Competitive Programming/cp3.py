def climbingLeaderboard(ranked, player):
    # Write your code here
    result = []
    for p in player:
        ranked.append(p)
        x = set(ranked)
        ranked = list(x)
        ranked.sort()
        ranked.reverse()
        temp = ranked.index(p)
        result.append(temp + 1)
    
    return result
    

print(climbingLeaderboard([100,100,50,40,40,20,10], [5,25,50,120]))