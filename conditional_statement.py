
# program for condition statements (if , if_else , if_elif_else)
a = int(input("Enter a value :")
b = int(input("Enter b value :")
c = int(input("Enter c value :")
if a > b and a > c :
   print("Largest element is a :" , a)
elif b > a and b > c :
   print("Largest element is b :" , b)
elif c > a and c > b :
   print("Largest element is c :" , c)
else :
   print("No element is found ")