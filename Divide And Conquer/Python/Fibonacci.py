def fib(n):
   if n == 1:
      return 1
   elif n == 0:   
      return 0            
   else:                      
      return fib(n-1) + fib(n-2) 

r = int(input("Enter number: "))
print(fib(r))

