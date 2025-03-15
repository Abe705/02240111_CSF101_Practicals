import math

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(start_range, end_range):
    total_sum = 0
    for n in range(start_range, end_range + 1):
        if is_prime_number(n):
            total_sum += n
    return total_sum

def convert_length(amount, conversion_type):
    if conversion_type.upper() == 'M':
        return round(amount * 3.28084, 2) 
    elif conversion_type.upper() == 'F':
        return round(amount / 3.28084, 2)  
    else:
        raise ValueError("Invalid conversion type. Use 'M' for meters to feet or 'F' for feet to meters.")

def count_consonants(input_text):
    vowel_set = "aeiouAEIOU"
    consonant_list = [char for char in input_text if char.isalpha() and char not in vowel_set]
    return len(consonant_list)

def find_min_max(*args):
    if not args:
        raise ValueError("At least one number must be provided.")
    smallest_value = min(args)
    largest_value = max(args)
    return f"Smallest: {smallest_value}, Largest: {largest_value}"

def is_palindrome(input_string):
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

def count_words_in_file(file_location, words_to_count):
    try:
        with open(file_location, 'r') as file:
            file_content = file.read().lower()
            word_count_dict = {word: file_content.split().count(word) for word in words_to_count}
            return word_count_dict
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_location} was not found.")
        
def main():
    words_to_count = ["the", "was", "and"]
    while True:
        print("\nAvailable Functions:")
        print("1. Prime Number Sum Calculator")
        print("2. Length Unit Converter")
        print("3. Count consonants in string")
        print("4. Find min and max numbers")
        print("5. Check for palindrome")
        print("6. Word Counter")
        print("0. Exit program")
        
        user_choice = input("\nEnter your choice: ").strip()
        
        try:
            if user_choice == '1':
                start_range = int(input("Enter the start of the range: "))
                end_range = int(input("Enter the end of the range: "))
                result = sum_of_primes(start_range, end_range)
                print(f"Sum of prime numbers in the range {start_range}-{end_range}: {result}")
            
            elif user_choice == '2':
                amount = float(input("Enter a numeric value: "))
                conversion_type = input("Enter conversion direction ('M' for meters to feet, 'F' for feet to meters): ").strip()
                result = convert_length(amount, conversion_type)
                print(f"Converted value: {result}")
            
            elif user_choice == '3':
                input_text = input("Enter a string: ")
                result = count_consonants(input_text)
                print(f"Number of consonants: {result}")
            
            elif user_choice == '4':
                numbers = list(map(int, input("Enter numbers separated by space: ").split()))
                result = find_min_max(*numbers)
                print(result)
            
            elif user_choice == '5':
                input_string = input("Enter a string: ")
                result = is_palindrome(input_string)
                print(f"Is palindrome: {result}")
            
            elif user_choice == '6':
                file_location = input("Enter the file path: ").strip()
                word_counts = count_words_in_file(file_location, words_to_count)
                print(f"Word counts: {word_counts}")
            
            elif user_choice == '0':
                print("Exiting program...")
                break
            
            else:
                print("Invalid choice, please enter a number between 0 and 6.")
        
        except ValueError as e:
            print(f"Error: {e}")
        except FileNotFoundError as e:
            print(f"Error: {e}")
        
        continue_choice = input("\nWould you like to try another function? (y/n): ").strip().lower()
        if continue_choice != 'y':
            break

if __name__ == "__main__":
    main()