# Function to convert weight from pounds to kilograms
def weight_converter(pounds):
    return pounds / 2.2  # 1 pound = 2.2 kilograms

# Function to convert height from feet and inches to centimeters
def height_converter(feet, inches):
    feet_to_inches = feet * 12  # Convert feet to inches
    height_in_inches = feet_to_inches + inches  # Total height in inches
    return height_in_inches * 2.54  # Convert inches to centimeters (1 inch = 2.54 cm)

# Function to get a positive integer input with validation
def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value  # Ensure value is positive
            else:
                print("Value must be greater than zero.")
        except ValueError:
            print("Please enter a valid number.")

# Function to get a non-negative integer (e.g., for inches which can be 0)
def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value  # Ensure value is non-negative
            else:
                print("Value must be 0 or greater.")
        except ValueError:
            print("Please enter a valid number.")

# Function to determine physical activity level with descriptions
def physical_activity_level():
    # Store activity levels in a dictionary for easier maintenance
    activity_levels = {
        1: "Little/no exercise (sedentary lifestyle)",
        2: "Light exercise 1-2 times a week",
        3: "Moderate exercise 2-3 times a week",
        4: "Hard exercise 4-5 times a week",
        5: "Physical job or hard exercise 6-7 times a week",
        6: "Professional athlete"
    }

    print("______________________________________________________")
    print("To determine your activity level, choose a number 1-6:")
    # Display activity level options
    for level, description in activity_levels.items():
        print(f"{level}--{description}")
    print("...")

    # Get user input for activity level and validate it
    activity_level = get_positive_int("Choose a number 1-6: ")
    while activity_level not in activity_levels:
        print("Invalid choice. Please choose a number between 1 and 6.")
        activity_level = get_positive_int("Choose a number 1-6: ")
    return activity_level

# Function to calculate BMR for both males and females
def calculate_BMR(gender):
    # Prompt user for weight, height, and age inputs with validation
    weight_lbs = get_positive_int("Weight (lbs): ")
    height_ft = get_positive_int("Height (ft): ")
    height_in = get_non_negative_int("Height (in): ")  # Allow 0 inches
    years = get_positive_int("Age: ")

    # Convert weight to kilograms and height to centimeters
    weight_kg = weight_converter(weight_lbs)
    height_cm = height_converter(height_ft, height_in)

    # Calculate and return BMR based on gender
    if gender.upper() == "M":
        return 66.5 + (13.75 * weight_kg) + (5.003 * height_cm) - (6.75 * years)
    else:
        return 655.1 + (9.563 * weight_kg) + (1.850 * height_cm) - (4.676 * years)

# Function to calculate total daily calories based on activity level and BMR
def total_daily_calories(BMR):
    # Get user's physical activity level
    activity_level = physical_activity_level()
    # Match activity level to appropriate multiplier
    match activity_level:
        case 1:
            return BMR * 1.2  # Sedentary
        case 2:
            return BMR * 1.375  # Light exercise
        case 3:
            return BMR * 1.55  # Moderate exercise
        case 4:
            return BMR * 1.725  # Hard exercise
        case 5:
            return BMR * 1.9  # Very hard exercise
        case 6:
            return BMR * 2.3  # Professional athlete

# Main program loop
while True:
    print("__________BMR CALCULATOR_________")
    # Prompt user for gender input with validation
    gender = input("Enter your Gender (M or F): ").strip().upper()
    while gender not in ["M", "F"]:
        gender = input("Invalid input. Please enter M or F: ").strip().upper()

    # Calculate BMR based on gender
    BMR = calculate_BMR(gender)

    # Calculate and display total daily calorie needs
    final_calories = round(total_daily_calories(BMR), 2)  # Round to 2 decimal places
    print("******************************************")
    print(f"Your Total Daily Calories: {final_calories} kcal")
    print("******************************************")

    # Ask if the user wants to calculate again
    repeat = input("Would you like to calculate again? (yes/no): ").strip().lower()
    if repeat != "yes":
        print("Thank you for using the BMR Calculator. Goodbye!")
        break
