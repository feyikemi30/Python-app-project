# app.py

def calculate_year_to_turn_100(name, age):
    from datetime import datetime
    
    # Get the current year
    current_year = datetime.now().year
    
    # Calculate the year in which the user will turn 100
    year_to_turn_100 = current_year + (100 - age)
    
    return year_to_turn_100
    

def main():
    # Ask the user for their name
    name = input("Please enter your name: ")
    
    # Ask the user for their age
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Please enter a valid age.")
        return
    
    # Calculate the year in which the user will turn 100
    year = calculate_year_to_turn_100(name, age)
    
    # Print the result
    print(f"{name}, you will turn 100 years old in the year {year}.")

if __name__ == "__main__":
    main()
