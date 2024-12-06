from itertools import permutations

# Generate a list with all the possible digit combinations of number_size digits
def generate_combinations(number_size):
    return [''.join(p) for p in permutations('0123456789', number_size)]

# Filter the numbers from the main list
def filter_numbers(posibles, tries, corrects, correct_position):
    return [
        number for number in posibles
        if (sum(1 for a, b in zip(tries, number) if a == b) == correct_position) and
           (sum(1 for digit in tries if digit in number) == corrects)
    ]

def play(number_size):
    possible_numbers = generate_combinations(number_size)

    # Keep playing until there is only 1 possible number
    while len(possible_numbers) > 1:
        print(f"\nThere are {len(possible_numbers)} posible numbers\n")
        attemp = input(f"Your guess ({number_size} digits): ")

        # Check that the number your typed is valid
        if len(attemp) != number_size or len(set(attemp)) != number_size or not attemp.isdigit():
            print("Use a correct value.")
            continue
        
        corrects = int(input("How many digits are correct? "))
        correct_position = int(input("How many of them are in the correct position? "))
        
        possible_numbers = filter_numbers(possible_numbers, attemp, corrects, correct_position)

    if possible_numbers:
        print(f"\nThe correct number is {possible_numbers[0]}")
    else:
        print("There are no valid answers, try again")

# Start of the main game
number_size = int(input("How many digits?: "))
play(number_size)
