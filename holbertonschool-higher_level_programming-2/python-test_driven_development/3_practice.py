# Example of a basic Python program using Test-driven Development
# This program will test the sum of two numbers

# Write the first test
def test_sum():
    assert sum(2,3) == 5

# Create the function to pass the test
def sum(a,b):
    return a + b

# Run the test
test_sum()

# If the test passes, you have successfully completed Test-driven Development!
