isbn = input("")
validChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', 'X']
controlNum = 0
validInputChars = True

for char in isbn:
    if not char in validChars:
        validInputChars = False

if len(isbn) == 10 and validInputChars:
    if '.' in isbn:
        dotindex = isbn.find('.')

        countdown = 10
        for char in isbn:
            if char == '.':
                char = 0
            controlNum+=int(char)*countdown
            countdown-=1

        countdown = 10
        for i in range(11):
            factor = countdown - dotindex
            if (controlNum + factor*i) % 11 == 0:
                if i == 10:
                    i = 'X'
                print(i)
                break
    else:
        countdown = 10
        for char in isbn:
            if char == 'X':
                char = 10
            controlNum+=int(char)*countdown
            countdown-=1

        print("VALID") if controlNum % 11 == 0 else print("INVALID")
else:
    print("INPUT ERROR")