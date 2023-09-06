# 1.1 implementing a recursive function to calculate the factorial of a given number

def fact(n):
  if n==0:
    return 1
  else:
    return n*fact(n-1)

n=int(input("enter the number:"))
result=fact(n)
print("Factorial of",n,"is",result)