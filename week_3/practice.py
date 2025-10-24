n=5
increment=""
for i in range(1,n+1):
        increment=increment+str(i)
        decrement=increment[::-1][1:]
        print(increment+decrement)
