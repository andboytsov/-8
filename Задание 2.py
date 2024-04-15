def reverse_number(num):
    return int(str(num)[::-1])

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def process_numbers(numbers):
    results = []
    for num in numbers:
        reversed_num = reverse_number(num)
        if is_palindrome(num):
            results.append(f"{num} is a palindrome")
        results.append(reversed_num)
    return results

numbers = [135, 175, 585, 195]
processed_numbers = process_numbers(numbers)
for item in processed_numbers:
    print(item)
