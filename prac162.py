#백준 2407
import sys
n,k=map(int,sys.stdin.readline().split())
dp=[1]*(n+1)
for i in range(2,n+1):
    dp[i]=dp[i-1]*i

print(dp[n]//(dp[n-k]*dp[k]))