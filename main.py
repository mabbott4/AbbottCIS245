def main():
    intro() 
    
    try:
        miles = int(input("Please enter number of miles: ")) # get number of miles
        miles_to_kilometers(miles)  
    except ValueError:
        print("An error occurred, please enter a number only.")
        print()
        main()

def intro():
    print("This program converts measurements in miles to kilometers.")
    print("For your reference, the conversion is 1 mile = 1.609 kilometers.")
    print()

def miles_to_kilometers(miles):  # convert miles to kilometers
    kilometers = miles * 1.60934
  # display total miles and kilometers 
    print(miles, "miles converts to", kilometers, "kilometers.")

main() #call the main function
#testing changes 
#testing 