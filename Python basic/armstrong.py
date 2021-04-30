num = int(input("enter a num"))
order = len(str(num))

sum = 0
temp =num
while(temp>0):
    digit = temp%10
    sum = sum+digit**order
    temp = temp//10

if num == sum:
    print("it is a armstrong numer")
else:
    print("it is nota  armstromng number")
