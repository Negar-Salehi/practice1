name = input("Please enter your name:")
lastname = input("Please enter your lastname:")
number = int(input("Please enter the number of lessons:"))
n = number+1
sum = 0
for x in range(1 , n):
    Mark = float(input("Please Enter Mark of Lesson:"))
    sum = sum + Mark
a = sum/number
print(a)
if a>=17:
    print ("Excellent")
elif 17>a>=12:
    print ("Good")
elif a < 12:
    print ("Failed")

