#Use a function to convert miles to kilometers
#Incorporate try and except blocks
def convert_distance():
    try:
#promt the user for the number of miles driven
        miles = int(input("Enter amount of miles driven: "))
        kilometers = miles * 1.609
        print(f"At {miles} miles, your distance in kilometers is: {kilometers}") 
    except ValueError:
        print("That is not a number.  Please enter a number")
#Call a function that converts miles to kilometers
convert_distance()