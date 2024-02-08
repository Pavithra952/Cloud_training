def identify_pattern(sequence):
    if all(isinstance(item, int) for item in sequence):
        
        diff = sequence[1] - sequence[0]
        for i in range(1, len(sequence) - 1):
            if sequence[i + 1] - sequence[i] != diff:
                return None, "Arithmetic progression"

        return sequence[-1] + diff, "Arithmetic progression"

    elif all(isinstance(item, str) and len(item) == 1 for item in sequence):
        
        if sequence[-1] != 'Z':
            return chr(ord(sequence[-1]) + 1), "Alphabetical progression"

    elif all(isinstance(item, str) and item[:-1].isalpha() and item[-1].isdigit() for item in sequence):
        
        prefix = ''.join([char for char in sequence[-1] if char.isalpha()])
        suffix = ''.join([char for char in sequence[-1] if char.isdigit()])
        return f'{prefix}{int(suffix) + 1}', "Alphanumeric progression"

    return None, "Pattern not recognized"


def get_user_input():
    try:
        user_input = input("Enter the sequence (comma-separated): ").split(',')
        sequence = [eval(item.strip()) if item.strip().isdigit() else item.strip() for item in user_input]
        return sequence
    except:
        print("Invalid input. Please enter a valid sequence.")
        return get_user_input()


# Continue taking sequences until the user chooses to stop
while True:
    user_sequence = get_user_input()

    result, pattern_type = identify_pattern(user_sequence)
    if result is not None:
        print(f"The next number in the sequence is: {result}")
        print(f"Identified pattern: {pattern_type}")
    else:
        print("Pattern not recognized.")

    continue_input = input("Do you want to continue? (y/n): ").lower()
    if continue_input != 'y':
        break
