# Initialize the database, knowbase, and color arrays
database = ['Croaks', "Eat Flies", "Shrimps", "Sings"]
knowbase = ["Frog", "Canary"]
color = ["Green", "Yellow"]

# Function to display the available object choices
def display_objects():
    print("\n X is: \n1. Frog \n2. Canary", end='')
    print("\nSelect one:", end='')

# Main function implementing backward chaining logic
def main():
    print("*-----Backward--Chaining-----*", end='')
    display_objects()  # Display object choices for user selection

    # Get user input and ensure it's a valid number
    try:
        x = int(input())
    except ValueError:
        print("\n---Invalid input! Please select a valid option between 1 and 2.")
        return

    # Check if the selected option corresponds to a valid object
    if x == 1:
        print("Chance of eating flies", end='')
    elif x == 2:
        print("Chance of shrimping", end='')
    else:
        print("\n---Invalid Option! Please select a valid option between 1 and 2.")
        return

    # If the option is valid (1 or 2), display more details
    if 1 <= x <= 2:
        print("\nObject is:", knowbase[x-1])  # Display selected object
        print("Color options: 1. Green  2. Yellow", end='')
        print("\nSelect color option:", end='')

        # Get color input from the user
        try:
            k = int(input())
        except ValueError:
            print("\n---Invalid input! Please select either option 1 or 2 for color.")
            return

        # Match the selected object and color to the correct fact
        if k == 1 and x == 1:  # Frog and Green
            print("Yes, it is in", color[0], "color and will", database[0])  # "Croaks"
        elif k == 2 and x == 2:  # Canary and Yellow
            print("Yes, it is in", color[1], "color and will", database[1])  # "Eat Flies"
        else:
            print("\n---Invalid Knowledge Database! Please select valid options.")

# Run the program
if __name__ == "__main__":
    main()
