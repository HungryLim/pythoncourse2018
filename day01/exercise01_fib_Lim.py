## Fibonacci sequence
## X_[i] = X_[i-1] + X_[i-2], where X_1 = 1, X_2 = 1
## 1,1,2,3,5,8,....

## Write a for loop, while loop, or function (or all three!) to create a
## list of the first 10 numbers of the fibonacci sequence

    
def fibo(n):
    x=[1,1]
    while len(x)<n:
        num=x[len(x)-1]+x[len(x)-2] #first one is the last one and the second one is the first one
        x.append(num)
    return x

fibo(10)
fibo(20)

    
def fibo2(n):
    x=[1,1]
    while len(x)<n:
        #first one is the last one and the second one is the first one
        x.append(x[-1]+x[-2])
    return x

fibo2(10)


