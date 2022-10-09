#Use a function to convert miles to kilometers
def convert_distance(miles):
    kilometers = miles * 1.609
#Display total miles and the kilometers
    print(f"At {miles} miles, your distance in kilometers is: {kilometers}")
print()
#Incorporate try and except blocks
miles = None
while miles is None:
    try:
#Prompt user for amount of miles driven
        print((miles:= int(input("Enter amount of miles driven: "))))
    except ValueError:
        print("That is not a number.  Please enter a number")
convert_distance(miles)

