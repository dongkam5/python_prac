#13699
n=int(input())

dp=[0]*(n+1)
dp[0]=1

for i in range(1,n+1):
    for j in range(i-1,-1,-1):
        dp[i]+=dp[j]*dp[i-1-j]
print(dp[n])