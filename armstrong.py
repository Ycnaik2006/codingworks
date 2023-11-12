def Armstrong(n):
    string = str(n)
    d = len(string)
    sum = 0

    for i in string:
        i = int(i)
        sum += i**d
    
    if sum == n:
        return 1
    else:
        return 0

n = int(input("Enter a number:"))
if n >= 100 and n <= 999:
    result = Armstrong(n)

    if result == 1:
        print(n, "is an Armstrong number.")
    else:
        print(n, "is not an Armstrong number.")
else:
    print("Invalid input. Please enter a three-digit number.")
