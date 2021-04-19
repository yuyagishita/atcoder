#写経
s=input()
N=len(s)
dp=[[0]*N for i in range(N)]
for w in range(2,N):
  for i in range(N-w):
    j=i+w
    for k in range(i+1,j+1):
      dp[i][j]=max(dp[i][j],dp[i][k-1]+dp[k][j])
    if s[i]==s[j]=='i':
      for k in range(i+1,j):
        if s[k]=='w' and dp[i+1][k-1]*3 == k-i-1 and dp[k+1][j-1]*3 == j-k-1:
          dp[i][j]=max(dp[i][k-1]+dp[k][j]+1,dp[i][j])
print(dp[0][N-1])
