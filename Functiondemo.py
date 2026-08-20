# """
# A complete demonstration of all function types in Python.
# """

# # 1. Standard Function (No parameters, no return)
# def greet():
#     print("1. Standard Function: Hello, World!")


# 2. Function with Parameters (Accepts inputs)
def greet_user(name):
    print(f"2. Parameter Function: Hello, {name}!")


# 3. Function with a Return Value (Sends data back)
# def add_numbers(a, b):
#     return a + b


# # 4. Function with Default Parameters (Optional inputs)
# def power(base, exponent=2):
#     return base ** exponent


# # 5. Arbitrary Arguments / *args (Accepts any number of positional inputs)
# def sum_all_numbers(*args):
#     # args behaves like a tuple
#     return sum(args)


# # 6. Keyword Arbitrary Arguments / **kwargs (Accepts any number of named inputs)
# def print_user_profile(**kwargs):
#     # kwargs behaves like a dictionary
#     print("6. Kwargs Function Output:")
#     for key, value in kwargs.items():
#         print(f"   - {key}: {value}")


# # 7. Lambda Function (Anonymous, single-line function)
# # Useful for quick mathematical operations or sorting data
# multiply = lambda x, y: x * y


# # 8. Recursive Function (A function that calls itself)
# def factorial(n):
#     if n <= 1:  # Base case to prevent infinite loops
#         return 1
#     return n * factorial(n - 1)


# # ==========================================
# # EXECUTING THE FUNCTIONS
# # ==========================================
# if __name__ == "__main__":
#     print("--- STARTING FUNCTION DEMONSTRATION ---\n")

#     # Call Type 1
#     greet()

#     # Call Type 2
greet_user("Alice")

#     # Call Type 3
    # result = add_numbers(5, 7)
    # print(f"3. Return Function Result: {result}")

#     # Call Type 4
#     print(f"4a. Default Parameter (used default 2): {power(4)}")
#     print(f"4b. Default Parameter (overrode with 3): {power(4, 3)}")

#     # Call Type 5
#     total = sum_all_numbers(10, 20, 30, 40)
#     print(f"5. *args Function Result: {total}")

#     # Call Type 6
#     print_user_profile(username="coder123", role="admin", status="active")

#     # Call Type 7
#     print(f"7. Lambda Function Result: {multiply(6, 7)}")

#     # Call Type 8
#     print(f"8. Recursive Function Result (Factorial of 5): {factorial(5)}")

#     print("\n--- DEMONSTRATION COMPLETE ---")
