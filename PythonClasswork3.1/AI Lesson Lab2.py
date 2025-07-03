1
# Initialize the database and knowbase arrays
database = ["Croaks", "Eat Flies", "Shrimps", "Sings"]
knowbase = ["Frog", "Canary", "Green", "Yellow"]

# Function to display available facts for selection
def display_facts():
    print("\n X is: \n1. Croaks \n2. Eat Flies \n3. Shrimps \n4. Sings", end='')
    print("\n\nSelect an option: ", end='')

# Main function that implements forward chaining logic
def main():
    print("*-----Forward--Chaining-----*", end='')
    display_facts()  # Display the facts for user selection

    # Get user input and ensure it's a valid number
    try:
        x = int(input())
    except ValueError:
        print("\n---Invalid input! Please select a valid option between 1 and 4.")
        return

    # Check if the input corresponds to a known fact about objects
    if x == 1 or x == 2:
        print("Chance of Frog", end='')
    elif x == 3 or x == 4:
        print("Chance of Canary", end='')
    else:
        print("\n---Invalid Option! Please select a valid option between 1 and 4.")
        return

    # If the option is valid (between 1 and 4), display more details
    if 1 <= x <= 4:
        print("\n X is:", database[x-1])  # Display the fact based on user selection
        print("\nColor is: 1. Green  2. Yellow", end='')
        print("\nSelect color option: ", end='')

        # Get the color input from the user
        try:
            k = int(input())
        except ValueError:
            print("\n---Invalid input! Please select either option 1 or 2 for color.")
            return

        # Match the selected fact and color to the correct object
        if k == 1 and (x == 1 or x == 2):  # Frog and Green
            print("Yes, it is", knowbase[0], "And Color is", knowbase[2])
        elif k == 2 and (x == 3 or x == 4):  # Canary and Yellow
            print("Yes, it is", knowbase[1], "And Color is", knowbase[3])
        else:
            print("\n---Invalid Knowledge Database! Please select valid options.")

# Run the program
if __name__ == "__main__":
    main()

