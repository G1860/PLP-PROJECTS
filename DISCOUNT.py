# Define the function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Test the function with different examples
print("Test 1: calculate_discount(1000, 25) →", calculate_discount(1000, 25))   # Expected: 750.0
print("Test 2: calculate_discount(500, 10) →", calculate_discount(500, 10))     # Expected: 500
print("Test 3: calculate_discount(200, 20) →", calculate_discount(200, 20))     # Expected: 160.0
print("Test 4: calculate_discount(1500, 5) →", calculate_discount(1500, 5))     # Expected: 1500
print("Test 5: calculate_discount(800, 30) →", calculate_discount(800, 30))     # Expected: 560.0
