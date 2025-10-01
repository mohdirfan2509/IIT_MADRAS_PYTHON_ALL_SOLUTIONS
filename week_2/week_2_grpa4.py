operation = input()
if operation=="odd_num_check":
    number=int(input())
    if number%2==1:
        print("yes")
    else:
        print("no")   
elif operation=="perfect_square_check":
    number=int(input())
    if int(number**0.5)**2==number:
        print("yes")
    else:
        print("no")
elif operation=="vowel_check":
    text=input().lower()
    if "a" in text or "e" in text or "i" in text or "o" in text or "u" in text:
        print("yes")
    else:
        print("no")    
elif operation=="divisibility_check": 
    number=int(input())
    if number%2==0:
        print("divisible by 2")        
    elif number%3==0:   
        print("divisible by 3") 
    elif number%2==0 and number%3==0:   
        print("divisible by 2 and 3") 
    else:
        print("not divisible by 2 and 3")   
elif operation=="palindrominator":  
    text=input()
    text=text+text[:len(text)-1][::-1] 
elif operation=="simple_interest":
    principal_amount=float(input())  
    n_years=int(input())
    if n_years<10:
        print(round(principal_amount*n_years*0.05/100))
    else:
        print(round(principal_amount*n_years*0.08/100))
else :
    print("Invalid Operation")

