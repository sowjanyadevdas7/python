a = int(input("enter a value:"))
b = int(input("enter b value:"))
def add(a , b):
    return(a + b)
def sub(a , b):
    return(a - b)
def mult(a , b):
    return(a * b)
def division(a , b):
    return(a // b)
def modulus(a , b):
    return(a % b)
print("select operation:")
print("1.add of a and b is:")
print("2.sub of a and b is:")
print("3.mult of a and b is:")
print("4.division of a and b is:")
print("5.modulus of a and b is:")
choice = input("enter choice(1/2/3/4/5)")
if choice == '1':
   print(a,"+",b,"=", add(a,b))
elif choice == '2':
   print(a,"-",b,"=", sub(a,b))
elif choice == '3':
   print(a,"*",b,"=", mult(a,b))
elif choice == '4':
   print(a,"//",b,"=", division(a,b))
elif choice == '5':
    print(a,"%",b,"==", modulus(a,b))
else:
   print("Invalid input")

output:
    enter a value: 10
enter b value: 20
select operation:
1.add of a and b is:
2.sub of a and b is:
3.mult of a and b is:
4.division of a and b is:
5.modulus of a and b is:
enter choice(1/2/3/4/5)1
10 + 20 = 30
