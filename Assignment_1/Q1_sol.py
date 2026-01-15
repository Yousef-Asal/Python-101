vals = [6, 13, 23, 33, 43, 55, 61, 82, 79, 83, 86, 97]

def divisors(num: int):
    divs = []
    if num < 1:
        print("Please provide a positive number")
        return divs
    
    for i in range(num):
        if num % (i+1) == 0:
            divs.append(i+1)
    
    return divs

def is_prime(num: int):
    divs = divisors(num)
    if len(divs) == 2:
        return True
    return False

for val in vals:
    prime = is_prime(val)
    print(f"Number is: {val}", f"- Prime: {prime}", sep='\n')
    if not prime :
        divs = divisors(val)
        divs.pop(0)
        print(f"- Divisors: {divs}")

    print("*" * 20)
        
