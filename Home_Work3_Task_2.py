while 1:
    try:
        number = int(input("Please insert a number four digits long:"))
        if len(str(number)) == 4:
            break
        else:
            print('Four digits long please.')
    except ValueError:
        print('Try again!')

# Find multiplication
    # first way
number_list = list(str(number))
number_mult = eval(f"{number_list[0]} * {number_list[1]} * {number_list[2]} * {number_list[3]}")
    # second way 
digit_4 = number%10
digit_3 = int((number%100 - digit_4) / 10)
digit_2 = int((number%1000 - digit_3*10 - digit_4) / 100)
digit_1 = int((number%10000 - digit_2*100 - digit_3*10 - digit_4) / 1000)
number_mult1 = digit_1 * digit_2 * digit_3 * digit_4
    # third way 
digit1 = number // 1000
digit2 = (number - digit1*1000) // 100
digit3 = (number - digit1*1000 - digit2*100) //10
digit4 = number - digit1*1000 - digit2*100 - digit3*10
number_mult2 = digit1 * digit2 * digit3 * digit4

if number_mult == number_mult1 == number_mult2:
    print("Multiplication of digits in number %d is %d." %(number, number_mult))
else:
    print('Multiplication Error')

# Reverse order
number_rev = int(str(number)[::-1])
print("Reverse order number {} is {}.".format(number, number_rev))

# Sorted order
    # first way
number_list1 = list(str(number))
number_list1.sort()
number_sor = int(''.join(number_list1))
    # second way
number_sor1 = int(''.join(sorted(str(number))))

if number_sor == number_sor1:
    print(f"Number {number} in sorted order is {number_sor}.")
else:
    print('Sorted Error')
