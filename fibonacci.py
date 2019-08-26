def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))  
nterms = int(input("How many terms? "))  
if nterms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(recur_fibo(i))  
output:
   How many terms? 12
Fibonacci sequence:
0
1
1
2
3
5
8
13
21
34
55
89
