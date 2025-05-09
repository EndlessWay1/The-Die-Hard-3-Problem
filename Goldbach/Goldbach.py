import sys

def main():
    # using cmd line arg
    L = True
    if len(sys.argv) == 2:
        try: 
            n = int(sys.argv[1])
            if n >= 0 and n%2 == 0:
                pass
            else:
                L = False
        except ValueError:
            L = False
    else:
        L = False

    # detecting correct uses
    if L == False:
        while True:
            try:
                n = int(input("What's the number? "))
                if n < 0:
                    print("Please put an positive interger")
                    continue
                if n%2 != 0:
                    print("Please put an even positive interger")
                    continue
                break
            except ValueError:
                print("Please put an interger")

    list_prime = listofprime(n)
    print(list_prime)
    arr = twosum(n, list_prime)
    print(f"The answer would be {arr[0]}, and {arr[1]}")

    sys.exit(0)


# Return a list of prime from n numbers
def listofprime(n:int):

    list_prime = [1]

    for j in range(2, n + 1):
        # detecting is_prime
        tf = True
        for i in range(2,j + 1):
            if j%i == 0 and j != i:
                tf = False
                break
        if tf == True:
            list_prime.append(j)
        continue

    return list_prime


# twosum
def twosum(n: int, i: list):
    for item in range(len(i)):
        res = n - i[item]
        for j in i[:item:-1]:
            if res == j:
                return (i[item], res)
    return False

if __name__ == "__main__":
    main()