
def doMath():
        name = input('Hello fellow classmate, please enter your name: ')
        try:
            name = name.isalpha()
            return name

        except ValueError:

       # if not name.isalpha():
            print("only letters: ")
    #except ValueError:
     #   print('Invalid input.  Make sure you have entered alphabets')
    
        #print('This is a simple program to display your name back to you and to do some math... but also introduce a bug...')
        # print('Let\'s do some math...')
        try:
            int1 = int(input('Please input the first integer: '))
            int2 = int(input('Please input the second integer: '))
            total = int1 * int2
            print(f'The first integer added to the second integer is: {total}')
        except ValueError:
            print('You must enter a number! Please run the program again!')
    

    #if not studentName.isalpha():
    #print("Only letters are allowed!")
doMath()