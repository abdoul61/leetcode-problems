#This is problem is called the climbin stairs
#The same as the fibonaci series


def func(n:int)->int:
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp)
    return dp[n]

def func2(n:int)->int:
    one,two = 1,1
    for i in range(n-1):
        temp = one
        one = one + two
        two = temp
    return one

print(func2(5))
print(func(5))
