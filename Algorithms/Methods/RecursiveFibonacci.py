def fib_digit(n):
    temp=[0 for i in range(n+1)]
    temp[1]=1
    for i in range(2,n+1):
        temp[i]=(temp[i-1]+temp[i-2])%10
    return temp[n]

def main():
    n = int(input())
    print(fib_digit(n))

if __name__ == "__main__":
    main()
