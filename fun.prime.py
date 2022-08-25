def prime_number():
    a=int(input("enter prime number"))
    i=0
    while i<=a:
        j=1
        count=0
        while j<=i:
            if i%j==0:
                count=count+1
            j=j+1
        if count==2:
            print(i)
        i=i+1
prime_number()


    
    
