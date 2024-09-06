# Day 1 - 30DaysOfPython Challenge

print(2 + 3)    # addition
print(3 - 1)    # subtraction
print(2 * 3)    # multiplication
print(3 / 2)    # division
print(3 ** 2)   # exponential
print(3 % 2)    # modulus
print(3 // 2)   # floor division

# checking data types
print(type(10))                 # Integer
print(type(3.14))               # Float
print(type(3 + 4j))             # Complex number
print(type("Felix"))            # String
print(type([1, 2, 3]))          # List
print(type({1, 2, 3}))          # set
print(type({"name": "Felix"}))  # Dictionary
print(type((1.5, 2, 3.14)))     # Tuple

x = (2, 3)
y = (10, 8)

euclid = ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5
print(euclid)