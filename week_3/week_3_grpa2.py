# # Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
# with open(__file__) as f:
#     content = f.read().split("# <eoi>")[2]
# if "while " in content:
#     print("You should not use while loop or the word while anywhere in this exercise")

# # your code should not use more than 7 for loops 
# # assuming one for loop per problem
# if content.count("for ")>7:
#     print("You should not use more than 7 for loops")

# # This is the first line of the exercise
# task = input()
# # <eoi>

# if task=="factorial":
#     num=int(input())
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i 
#     print(fact)
# elif task=="even_numbers":
#     num=int(input())
#     for i in range(0,num+1,2):
#         print(i)
# elif task=="power_sequence":
#     num=int(input())
#     for i in range(1,num+1):
#         print(2**i)
# elif task=="sum_not_divisible":
#     n=int(input())
#     sum=0
#     for i in range(0,n):
#         if i>0 and i%4 != 0 and i%5 != 0:
#             sum=sum+i
#         else:
#             pass            
#     print(sum)
# elif task=="from_k":
#     n=int(input())
#     k=int(input())
#     count=0
#     for i in range(k,0,-1):
#         if i%2==1 and "5" not in str(i) and "9" not in str(i):
#             print(str(i)[::-1])
#         if count==n:
#             break
# elif task=="string_iter":
#     s=input()
#     prev=1
#     for i in range(len(s)):
#         curr=int(s[i])
#         print(curr*prev)
#         prev=curr
# elif task=="list_iter":
#     l1=eval(input())
#     for  i in l1:
#         print(f"{i} - {type(i)}")
#     print(l1)
# else:
#     print("Invalid")    

# ****************************************

# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "while " in content:
    print("You should not use while loop or the word while anywhere in this exercise")

# your code should not use more than 7 for loops 
# assuming one for loop per problem
if content.count("for ")>7:
    print("You should not use more than 7 for loops")

# This is the first line of the exercise
task = input()
# <eoi>

if task=="factorial":
    n=int(input())
    result=1
    for i in range(1,n+1):
        result=result*i
    print(result)  
elif task=="even_numbers":
    n=int(input())
    for i in range(0,n+1,2):
        print(i)      
elif task=="power_sequence":
    n=int(input())
    for i in range(1,n+1):
        print(2**i)
elif task==""        


        
        
                 
