n=int(input())

dp=[0]*100
dp[0]=0
dp[1]=1
def fibo(num):
    for i in range(2,num+1):
        dp[i]=(dp[i-1]+dp[i-2])
    return dp[num]

print(fibo(n))