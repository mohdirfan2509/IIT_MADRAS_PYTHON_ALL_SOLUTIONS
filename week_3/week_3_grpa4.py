# this is to ensure that you cannot use the built in any, all and min function for this exercise but you can use it in the OPPEs.
any = None 
all = None
min = None 

task = input()
if task=="factors":
    n=int(input)
    if n>0:
        for i in range(1,n+1):
            if n%i==0:
                print(i)
elif task=="find_min":
    n=int(input())
    minimum=float('inf')
    for i in range(1,n+1):
        num=int(input())
        minimum=min(minimum,num)
    print(minimum)    
elif task=="prime_check":
    n=int(input())
    is_prime=True
    for i in range(2,int(n**0.5)+1):
            if n%i==0:
                is_prime=False
    print(is_prime)           
elif task=="is_sorted":
    word=input()
    flag=True
    for i in range(0,len(word)-1):
        if word[i]>word[i+1]:
            flag=False
    print(flag)        
elif task=="any_true":
    n=int(input())
    flag=False
    for i in range(0,n+1):
        num=int(input())
        if num%3==0:
            flag=True
    print(flag)  
elif task=="manhattan":
    dir=input()
    x_cord=0
    y_cord=0
    while dir !='STOP':
        if dir=='UP':
            y_cord=y_cord+1
        if dir=='DOWN':
            y_cord=y_cord-1
        if dir =='LEFT':
            x_cord=x_cord-1
        if dir=='RIGHT':
            x_cord=x_cord+1
        dir=input()   
    print(abs(x_cord)+abs(y_cord))
                                 

                
                
    