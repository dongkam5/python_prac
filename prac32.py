n=int(input())
lst=[0]+list(map(int,input().split()))
dp=lst
for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i]=min(dp[i],dp[i-j]+lst[j])

print(dp[n])