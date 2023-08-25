num=int(input("Enter a number:"))

if num<0:
    print("Sorry the factorial does not exist for negative numbers")
elif num==0:
    print("The factorial of 0 is 1")
else:
  for i in range(1, num+1):
   factorial=factorial*1
print("the factorial of",num,"is",factorial)