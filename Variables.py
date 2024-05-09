# 1. Create a variable named pi and store the value 22/7 in it. Now check the data type of this variable.
pi = 22/7
print("Data type of pi:", type(pi))

# 2. Create a variable called for and assign it a value 4. See what happens and find out the reason behind the behavior that you see.
# This will result in a syntax error because 'for' is a reserved keyword in Python and cannot be used as a variable name.

# 3. Store the principal amount, rate of interest, and time in different variables and then calculate the Simple Interest for 3 years. Formula: Simple Interest = P x R x T / 100
principal_amount = 2000
rate_of_interest = 10
time = 3

simple_interest = (principal_amount * rate_of_interest * time) / 100
print("Simple Interest:", simple_interest)
