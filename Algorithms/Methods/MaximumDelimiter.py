def NOD(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    elif a>=b:
        return NOD(a%b,b)
    elif b>=a:
        return NOD(a,b%a)


def main():
    a, b = map(int, input().split())
    print(NOD(a, b))


if __name__ == "__main__":
    main()
