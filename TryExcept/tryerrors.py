def convert_distance():
    try:
        miles = int(input("Enter amount of miles driven: "))
        kilometers = miles * 1.609
        print(f"At {miles} miles, your distance in kilometers is: {kilometers}") 
    except ValueError:
        print("That is not a number.  Please enter a number")
convert_distance()