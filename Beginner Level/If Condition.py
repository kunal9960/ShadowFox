# 1. Write a program to determine the BMI Category based on user input.

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi = weight / (height ** 2)

if bmi >= 30:
    category = "Obesity"
elif 25 <= bmi < 30:
    category = "Overweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
else:
    category = "Underweight"

print("Output:", category)

# 2. Write a program to determine which country a city belongs to. Given list of cities per country:

Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name: ")
if city in Australia:
    country = "Australia"
elif city in UAE:
    country = "UAE"
elif city in India:
    country = "India"
else:
    country = "Unknown"

print("Output:", city, "is in", country)

# 3. Write a program to check if two cities belong to the same country. Ask the user to enter two cities and print whether they belong to the same country or not.

Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

if city1 in Australia and city2 in Australia:
    country = "Australia"
elif city1 in UAE and city2 in UAE:
    country = "UAE"
elif city1 in India and city2 in India:
    country = "India"
else:
    country = None

if country:
    print("Both cities are in", country)
else:
    print("They don't belong to the same country")
