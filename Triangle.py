print("Drawing Triangle")
print("Enter the first side")
a = float(input())
print("Enter the second side")
b = float(input())
print("Enter the third side")
c = float(input())
if a < 0 or b < 0 or c < 0 :
    print(" It is not possible")
elif a==0 or b==0 or c==0 :
    print(" It is not possible")
elif a>b+c or b>a+c or c>a+b :
    print(" You can draw triangle")