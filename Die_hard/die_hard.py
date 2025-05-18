import sys

def main():
    # Ensuring correct usage
    while True:

        try:
            First = int(input("What's in the first jug?(Gallons) "))
            if First <= 0:
                raise ValueError
        except ValueError:
            print("The First jug must be a natural number" )
            continue

        try:
            Second = int(input("What's in the second jug?(Gallons) "))
            if Second <= 0:
                raise ValueError
            break
        except ValueError:
            print("The Second jug must be an natural number")
    # Switching Variable
    if Second > First:
        a,b = First, Second
        First = "second"
        Second = "first"
    else:
        a,b = Second, First
        First = "first"
        Second = "second"    

    # getting the linear combinations
    t, s, GCD = linear_combination(a,b)
    #print(f"\nLinear Combination: {GCD} = ({s})*({a}) + ({t})*({b}) \n")
    
    # making sure s is positive
    while s < 0:
        s = s + b
        t = t - a
    
    #print(f"\nLinear Combination: {GCD} = ({s})*({a}) + ({t})*({b}) \n")
    
    # how much do you need to fill
    while True:
        try:
            n = int(input("How much do you need to fill?(Gallons) "))
            if n <= 0:
                raise ValueError
            if n > b:
                print(f"It's impossible because the number of gallons needed exceeded the jug limits by {abs(b - n)}")
                sys.exit(0)

            q, rem = quotient_remainders(GCD, n) # making sure n | GCD 
            if rem != 0:
                print(f"It's impossible because the number of gallons needed must be a multiple of the Greatest Common Divisor, which is {GCD}")
                sys.exit(0)
            break
        except ValueError:
            print(f"The number must be a natural number")
    
    # printing the linear equations
    #print(f"\nLinear Combination: {GCD*q} =  ({s*q})*({a}) + ({t*q})*({b})\n")

    # end result
    print("___***___")
    print(f"You need to fill the {Second} jug exactly {s*q} times, and everytime it is full, we pour to the {First} jug. If when poured the {First} jug is full, dont throw the excess water from the {Second} jug away. We throw out the water from the {First} jug and pour the excess water from the {Second} jug back to the {First} jug. When done correctly we should throw out the water only {abs(t*q)} times. In the end we should ended up with {GCD*q} gallons of water.")
    print("___***___")


# return the quotient and the remainders
def quotient_remainders(a: int, b: int):
    
    q = 0
    while b >= a:
        q += 1
        b -= a
    
    return (q, b)


# return the greatest common divisor using the Euclid’s Algorithm
def gcd(b, a):
    r = b % a
    if r == 0:
        return a
    return gcd(a, r)
    

# return the pulverizer or in other words the linear combinations where L = ta + sb, or more commonly known as the extended Euclidean GCD algorithm
def linear_combination(a, b):
    prev_r, r = b, a
    prev_s, s = 0, 1
    prev_t, t = 1, 0

    while r != 0:
        q, rem = quotient_remainders(r, prev_r)
        prev_r, r = (r, rem)
        prev_t, t = (t, prev_t - q * t)
        prev_s, s = (s, prev_s - q * s)
    return (prev_t, prev_s, prev_r)


if __name__ == "__main__":
    main()