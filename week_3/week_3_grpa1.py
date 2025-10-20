# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "for " in content:
    print("You should not use for loop or the word for anywhere in this exercise")

# This is the first line of the exercise
task = input()
# <eoi>

if task=="sum_until_0":
    total=0
    n=int(input())
    while n!=0:
        total=total+n
        n=int(input())
    print(total)
elif task=="total_price":
    total_price=0
    while True:
        line=input()
        if line=='END':
            break
        quantity,price=line.split()
        quantity,price=int(quantity),int(price)
        total_price=total_price+(quantity*price)
    price(total_price)    
elif task=="only_ed_or_ing":
    while True:
        line=input()
        if line.upper== 'STOP':
            break
        if line.lower.endswith("ed") or line.lower.endswith("ing"):
            print(line)
elif task=="reverse_sum_palindrome":
    number=int(input())
    while number!= -1:
        if number>0:
            sum=number+int(str(number)[::-1])
            if str(sum)[::-1]==str(sum):
                print(number)
            else:
                pass    
        else:
            pass
        number=int(input())  
elif task=="double_string":    
    line=input()
    while line!=" ":
        repeatedTwice=line*2
        print(repeatedTwice)
        line=input()
elif task=="odd_char":
    line=input()
    while not line.endswith("."):
        line=line[::2] 
        print(line,end=' ')
        line=input()
elif task=="only_even_squares":
    n=input()
    while (n!="NAN"):
        if int(n)%2==0:
            print(int(n)**2)
        else:
            pass
        n=input()
elif task=="only_odd_lines":
    n=input()
    while n!="END":
        new_line=new_line+n+ ' '
        n=input()
    split_line=new_line.split()[::2][::-1]
    reversed_line='\n'.join(split_line)
    print(reversed_line)

