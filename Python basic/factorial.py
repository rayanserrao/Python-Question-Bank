def fact(num):
    return 1 if (num ==0 or num == 1) else num*fact(num-1)

print(fact(5))