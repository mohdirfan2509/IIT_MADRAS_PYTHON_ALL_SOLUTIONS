age = int(input()) # int: Read a number as integer from standard input
dob = str(input()) # str: Read a string of format dd/mm/yy from standard input
day, month, year = int(dob.split("/")[0]),int(dob.split("/")[1]),int(dob.split("/")[2]) # int, int, int: Get the correct parts from dob as int

fifth_birthday = str(day)+"/"+str(month)+"/"+str(year+5) # str: fifth birthday formatted as day/month/year 

last_birthday = str(day)+"/"+str(month)+"/"+str(year+age)  # str: last birthday formatted as day/month/year

total_month = month + 10
new_month = total_month % 12
if new_month == 0:
    new_month = 12
new_year = year + (total_month - 1) // 12  # integer division
tenth_month = f"{day}/{new_month}/{new_year}" # str: dob same day after 10 months formatted as day/month/year

# print tenth_month, fifth_birthday and last_birthday in same line separated by comma and a space
print(tenth_month+", "+fifth_birthday+", "+last_birthday)

weight = float(input()) # float: Read a number as float from stdin(Standard input)
kg=int(weight)
grams=int(round((weight-kg)*1000))
weight_readable = f"{kg} kg {grams} grams" # str: reformat weight of format 55 kg 250 grams

# print weight_readable 
print(weight_readable)
