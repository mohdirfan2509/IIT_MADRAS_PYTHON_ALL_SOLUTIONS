# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "for " in content:
    print("You should not use for loop or the word for anywhere in this exercise")

# This is the first line of the exercise
task = input()
# <eoi>

if task == "sum_until_0":
    total = 0
    n = int(input())
    while n != 0:
        total += n
        n = int(input())
    print(total)

elif task == "total_price":
    total_price = 0
    while True:
        line = input()
        if line == "END":
            break
        quantity, price = line.split()
        total_price += int(quantity) * int(price)
    print(total_price)

elif task == "only_ed_or_ing":
    result = []
    s = input()
    while s.lower() != "stop":
        if len(s) >= 2 and (s[-2:].lower() == "ed" or s[-3:].lower() == "ing"):
            result.append(s)
        s = input()
    # Print each string on a new line
    i = 0
    while i < len(result):
        print(result[i])
        i += 1

elif task == "reverse_sum_palindrome":
    def is_palindrome(num):
        str_num = str(num)
        rev = ""
        i = len(str_num) - 1
        while i >= 0:
            rev += str_num[i]
            i -= 1
        return str_num == rev

    result = []
    n = int(input())
    while n != -1:
        rev = int(str(n)[::-1])
        if is_palindrome(n + rev):
            result.append(n)
        n = int(input())

    i = 0
    while i < len(result):
        print(result[i])
        i += 1

elif task == "double_string":
    line = input()
    while line != "":
        print(line * 2)
        line = input()

elif task == "odd_char":
    result = []
    s = input()
    while not s.endswith("."):
        filtered = ""
        i = 0
        while i < len(s):
            filtered += s[i]
            i += 2
        result.append(filtered)
        s = input()
    # Include last string ending with "."
    filtered = ""
    i = 0
    while i < len(s):
        filtered += s[i]
        i += 2
    result.append(filtered)

    # Print space-separated
    i = 0
    output = ""
    while i < len(result):
        if i != 0:
            output += " "
        output += result[i]
        i += 1
    print(output)

elif task == "only_even_squares":
    result = []
    n = input()
    while n != "NAN":
        num = int(n)
        if num % 2 == 0:
            result.append(num * num)
        n = input()
    i = 0
    while i < len(result):
        print(result[i])
        i += 1

elif task == "only_odd_lines":
    lines = []
    line_count = 1
    n = input()
    while n != "END":
        if line_count % 2 == 1:
            lines.insert(0, n)  # prepend to reverse order
        line_count += 1
        n = input()
    i = 0
    while i < len(lines):
        print(lines[i])
        i += 1
