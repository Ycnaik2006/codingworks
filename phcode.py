ph=float(input('Enter your ph level:'))
if ph <7.0 and ph>=0.0:
    print(ph, "is acidic.")

elif ph>7.0 and ph<=14.0:
    print(ph,"is basic.")

elif ph==7.0:
print(ph,"is neutral")
else:
print("Wrong input! ph value can only be between 0 and 14 only")

print("Thank you")