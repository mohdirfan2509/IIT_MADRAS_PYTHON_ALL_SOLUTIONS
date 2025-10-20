main_dish=input()
time_of_day=int(input())
has_voucher=bool(input())
is_card_payment=bool(input())

if main_dish=="paneer tikka":
    cost=250
elif main_dish=="butter chicken":  
    cost=240
elif main_dish=="masala dosa": 
    cost=200
else :
    print("Invalid dish") 
    exit()

if 12<=time_of_day<=15:
    total_cost=(1-0.15)*cost
else:
    total_cost=cost

if has_voucher:
    total_cost=total_cost+(1-0.10)*total_cost

if is_card_payment:
    total_cost=total_cost+ 0.05

print(f"{total_cost:.02f}")

