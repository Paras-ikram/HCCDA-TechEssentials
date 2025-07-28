# BMI Calculator with feet-to-meters conversion and detailed category info

# Step 1: Take user input
height_feet = float(input("Enter your height in feet: "))
weight_kg = float(input("Enter your weight in kilograms: "))

# Step 2: Convert height to meters (1 foot = 0.3048 meters)
height_meters = height_feet * 0.3048

# Step 3: Calculate BMI
bmi = weight_kg / (height_meters ** 2)

# Step 4: Print BMI value and category with explanation
print(f"\nYour BMI is: {bmi:.2f}")

# Step 5: Evaluate BMI Category
if bmi < 18.5:
    print("Category: Underweight")
    print("You are below the healthy weight range. It's recommended to consult a doctor or nutritionist to maintain a healthy weight.")
elif 18.5 <= bmi < 24.9:
    print("Category: Normal weight")
    print("You are within the healthy weight range. Maintain your current lifestyle and stay active!")
elif 25 <= bmi < 29.9:
    print("Category: Overweight")
    print("You are above the recommended weight range. Consider a balanced diet and regular exercise.")
else:
    print("Category: Obese")
    print("Your weight is in the obese range. It is strongly recommended to seek medical advice and adopt a healthier lifestyle.")
