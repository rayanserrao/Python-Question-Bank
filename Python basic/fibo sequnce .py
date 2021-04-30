def fibo(num):
    n1,n2 = 0,1
    count =0
    if num<0:
        print("Invalid number")
    elif num ==1:
        print(n1)
    else:
        while(count<num):
            print(n1)
            c = n1+n2
            n1, n2 = n2,c
            count+=1
    
fibo(5)
    
