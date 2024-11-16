# Function to calculate BMI
def calculate_bmi(weight, height):
    # BMI formula: weight (kg) / height (m)²
    bmi = weight / (height ** 2)
    return bmi

# Function to classify BMI
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Main program
def main():
    # Get user input for weight and height
    print("Welcome to the BMI Calculator!")
    weight = float(input("Enter your weight (in kilograms): "))
    height = float(input("Enter your height (in meters): "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Classify BMI
    classification = classify_bmi(bmi)

    # Output the result
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Classification: {classification}")

# Run the program
if __name__ == "__main__":
    main()
