task = input()
if task=="permutation":
    n=input()
    for i in n:
        for j in n:
            if i!=j:
                print(f'{i}{j}')
elif task=="sorted_permutation":
    n=input()
    for i in n:
        for j in n:
            if i!=j and i<j:
                print(f'{i}{j}')
elif task=="repeat_the_repeat":
    n=int(input())
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(j,end=' ')
        print()    
elif task=="repeat_incrementally":
    n=int(input())
    for i in range(1,n+2):
        for j in range(1,i):
            print(j,end=' ')
    print(end="\n")    
elif task=="increment_and_decrement":
    n=int(input())
    increment=' '
    for i in range(1,n+1):
        increment=increment+str(i)
        decrement=increment[::-1][1:]
        print(increment+decrement)



