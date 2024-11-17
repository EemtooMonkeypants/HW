def is_digit_pangram(input_string):
    digits = '0123456789'
    
    for digit in digits:
        if digit not in input_string:
            return False  
    
    return True  

input_string = input("Enter a string: ")

if is_digit_pangram(input_string):
    print("The input string is a digit pangram.")
else:
    print("The input string is not a digit pangram.")

