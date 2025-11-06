for number in range(1, 101):
    if not number % 3 == 0 and not number % 5 == 0:
        print(number)
    else:
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")  
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")