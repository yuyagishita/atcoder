A,B=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
dp=[[0]*(B+1) for i in range(A+1)]

for i in range(A+1):
    for j in range(B+1):
        if i+j==0:
            continue
        elif j==0:
            dp[i][j]=a[A-i]-dp[i-1][j]
        elif i==0:
            dp[i][j]=b[B-j]-dp[i][j-1]
        else:
            dp[i][j]=max(a[A-i]-dp[i-1][j],b[B-j]-dp[i][j-1])
print((sum(a)+sum(b)+dp[A][B])//2)
