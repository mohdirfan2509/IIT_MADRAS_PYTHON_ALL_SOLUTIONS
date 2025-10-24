# # this is to ensure that you cannot use the built in any, all and min function for this exercise but you can use it in the OPPEs.
# any = None 
# all = None
# min = None 

# task = input()
# if task=="factors":
#     n=int(input)
#     if n>0:
#         for i in range(1,n+1):
#             if n%i==0:
#                 print(i)
# elif task=="find_min":
#     n=int(input())
#     minimum=float('inf')
#     for i in range(1,n+1):
#         num=int(input())
#         minimum=min(minimum,num)
#     print(minimum)    
# elif task=="prime_check":
#     n=int(input())
#     is_prime=True
#     for i in range(2,int(n**0.5)+1):
#             if n%i==0:
#                 is_prime=False
#     print(is_prime)           
# elif task=="is_sorted":
#     word=input()
#     flag=True
#     for i in range(0,len(word)-1):
#         if word[i]>word[i+1]:
#             flag=False
#     print(flag)        
# elif task=="any_true":
#     n=int(input())
#     flag=False
#     for i in range(0,n+1):
#         num=int(input())
#         if num%3==0:
#             flag=True
#     print(flag)  
# elif task=="manhattan":
#     dir=input()
#     x_cord=0
#     y_cord=0
#     while dir !='STOP':
#         if dir=='UP':
#             y_cord=y_cord+1
#         if dir=='DOWN':
#             y_cord=y_cord-1
#         if dir =='LEFT':
#             x_cord=x_cord-1
#         if dir=='RIGHT':
#             x_cord=x_cord+1
#         dir=input()   
#     print(abs(x_cord)+abs(y_cord))

# *****************************************

task = input()

if task=="factors":
    n=int(input())
    for i in range(1,n+1):
        if n%i==0 and n>0:
            print(i)
elif task=="find_min":  
    n=int(input())
    minimum=float('inf')
    for i in range (1,n+1):
        number=int(input())
        minimum=min(minimum,number)
    print(minimum)
elif task=="prime_check":
    n=int(input())
    is_Prime=True
    for i in range(2,(i**0.5)+1):
        if i%2==0:
            is_Prime=False
    print(is_Prime)
elif task=="is_sorted":
    s=input()
    is_sorted=True
    for i in range(len(s)-1):
        if s[i]>a[i+1]:
            is_sorted=False  
            break 
    print(is_sorted)
elif task=="any_true":
    n=int(input)
    isDivisibleBy_3=False
    for i in range(n):
        num=int(input)
        if num%3==0:
            isDivisibleBy_3=True
    print(isDivisibleBy_3)    
elif task=="manhattan":
    direction=input()
    x_distance=0
    y_distance=0
    while direction!="STOP":
        if direction=="LEFT":
            x_distance-=1
        elif direction=="RIGHT":
            x_distance+=1
        elif direction=="UP":
            y_distance+=1
        elif direction=="DOWN":
            y_distance-=1
    x,y=abs(x_distance-0),(y_distance-0)
    manhattan_distance=x+y
    direction=input()
print(manhattan_distance)                    


    

                                 

                
                
    