def Pronic(n):
    for i in range(1,n+1):
        if i*(i+1)==n:
            return 1
    return 0
def main():
    n=int(input("Enter a number:"))
    result=Pronic(n)

    if result==1:
        print(n,"is a pronic number.")
    else:
        print(n,"is not a pronic number.")

if __name__=="__main__":
 main()
