# ╔═════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                 ║
# ║  Title:        prime_numbers.py                                                 ║
# ║  Author:       Group 1: The Prime Factors                                       ║
# ║  Team Members: Isa Mancuso, Ali Nur, Zabir Saif, Nathan Scrivens, Bob Wilson    ║
# ║  Date:         4-14-24                                                          ║
# ║  Homework:     Project Codeway                                                  ║
# ║  Description:                                                                   ║
# ║                Finds prime or composite numbers within a certain range.         ║
# ║                Also generates an exact amount of prime or composite numbers.    ║
# ║                Option to launch wikipedia webpage about prime numbers.          ║
# ║  Special Concerns:                                                              ║
# ║                    This app has not been tested on large ranges of numbers.     ║
# ║                    If the user enters a range of over 1 million numbers,        ║
# ║                    it might crash or take a really long time to calculate.      ║
# ║                                                                                 ║
# ╚═════════════════════════════════════════════════════════════════════════════════╝

import webbrowser

def input_int(input_string: str, at_least: int = None) -> int:
    """Asks the user to enter an integer that is at least at_least (unless at_least is None).
       If the user anything else, it keeps asking until it gets an integer"""
    num = None
    while num == None:
        num = input(input_string)
        try:
            num = int(float(num))
            if at_least != None and num < at_least:
                print(f'{num} is less than {at_least}!')
                num = None
            else: return num
        except (EOFError, KeyboardInterrupt): exit()
        except:
            print(num, 'is not a number!')
            num = None


def smallest_factor(num: int) -> int:
    """Accepts an integer 2 or greater, returns its smallest factor.
       If it has no factors, it is a prime number and it returns itself."""
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0: return divisor
    return num


def is_prime(num: int) -> bool:
    """Returns True if num is a prime number, False if it is not"""
    return smallest_factor(num) == num


def factorize(num: int) -> str:
    """Accepts an integer 2 or greater, returns a string listing all of the factors and their powers."""
    # First convert the number into a dictionary. The keys are factors, and the values are their powers.
    # For example, the number 40 (which is 2^3 * 5) creates the dictionary {2:3, 5:1}
    # Then convert the dictionary into a printable string. For example, {2:3, 5:1} becomes '40 = 2^3 * 5'
    factors = {}
    factors_string = f'{num} = '
    while num > 1:
        factor = smallest_factor(num)
        factors[factor] = factors.get(factor, 0) + 1
        num = num // factor
    for factor in factors:
        power = factors[factor]
        if power == 1: factors_string += f'{factor} * '
        else: factors_string += f'{factor}^{power} * '
    return factors_string[:-3]


def yes_or_no(print_string: str) -> bool:
    """Asks user a question, returns True if 'y' or 'yes' (case insensitive), otherwise returns False"""
    return input(print_string).lower() in ['y', 'yes']


def primes_in_range():
    """Asks user for two numbers, and finds all prime numbers between them"""
    repeat = True
    while repeat:
        print('\n─────────────────────────────────────────────────────────\n')
        print("Please enter two numbers, and I'll find all prime numbers between them.")
        minimum = input_int('Please enter a number: ')
        maximum = input_int('Please enter another number: ')
        if maximum < minimum: minimum, maximum = maximum, minimum
        print()
        if minimum == maximum and minimum > 1:
            if is_prime(minimum): print(minimum, 'is a prime number.')
            else:
                print(f'{minimum} is not a prime number.')
        else:
            primes = []
            for number in range(max(2, minimum), max(2, maximum + 1)):
                if is_prime(number): primes += [number]
            if primes == []:
                print(f'There are no prime numbers between {minimum} and {maximum}.')
                if maximum < 2: print('(2 is the smallest prime number.)')
            elif len(primes) == 1: 
                print(f'{str(primes)[1:-1]} is the only prime number between {minimum} and {maximum}.')
            else:
                print(f'Here are the {len(primes)} prime numbers between {minimum} and {maximum}:')
                print(str(primes)[1:-1])
        repeat = yes_or_no('\nWould you like to enter a new set of numbers? (Y or N)? ')


def generate_primes():
    """Asks user for an amount of prime numbers to generate, and what number to start searching at"""
    repeat = True
    while repeat:
        print('\n─────────────────────────────────────────────────────────\n')
        number_of_primes = input_int('How many prime numbers would you like me to generate? ', 1)
        primes = []
        minimum = input_int('What number would you like me to start searching at? ')
        number = max(2, minimum)
        while len(primes) < number_of_primes:
            if is_prime(number): primes.append(number)
            number += 1
        if number_of_primes == 1:
            print(f'\n{str(primes)[1:-1]} is the first prime number greater than or equal to {minimum}.')
        else:
            print(f'\nHere are the first {len(primes)} prime numbers greater than or equal to {minimum}:')
            print(str(primes)[1:-1])
        repeat = yes_or_no('\nWould you like to enter a new set of numbers? (Y or N)? ')


def composites_in_range():
    """Asks user for two numbers, and finds all composite numbers between them"""
    repeat = True
    while repeat:
        print('\n─────────────────────────────────────────────────────────\n')
        print("Please enter two numbers, and I'll find all composite numbers between them.")
        minimum = input_int('Please enter a number: ')
        maximum = input_int('Please enter another number: ')
        if maximum < minimum: minimum, maximum = maximum, minimum
        print()
        if minimum == maximum and minimum > 1:
            if is_prime(minimum): print(minimum, 'is not a composite number.')
            else: print(f'{minimum} is a composite number: {factorize(minimum)}')
        else:
            composites = []
            for number in range(max(2, minimum), max(2,maximum + 1)):
                if not is_prime(number): composites += [number]
            if composites == []:
                print(f'There are no composite numbers between {minimum} and {maximum}.')
                if maximum < 4: print('(4 is the smallest composite number.)')
            elif len(composites) == 1:
                print(f'{str(composites)[1:-1]} is the only composite number between {minimum} and {maximum}.')
                print(factorize(composites[0]))
            else:
                print(f'Here are the {len(composites)} composite numbers between {minimum} and {maximum}:')
                print(str(composites)[1:-1])
                if yes_or_no('\nWould you like to see their prime factors? (Y or N)? '):
                    print()
                    for composite in composites: print(factorize(composite))
        repeat = yes_or_no('\nWould you like to enter a new set of numbers? (Y or N)? ')


def generate_composites():
    """Asks user for an amount of composite numbers to generate, and what number to start searching at"""
    repeat = True
    while repeat:
        print('\n─────────────────────────────────────────────────────────\n')
        number_of_composites = input_int('How many composite numbers would you like me to generate? ', 1)
        composites = []
        minimum = input_int('What number would you like me to start searching at? ')
        number = max(2, minimum)
        while len(composites) < number_of_composites:
            if not is_prime(number): composites.append(number)
            number += 1
        if number_of_composites == 1:
            print(f'\n{str(composites)[1:-1]} is the first composite number greater than or equal to {minimum}.')
            if yes_or_no('\nWould you like to see its factors? (Y or N)? '):
                print()
                print(factorize(composites[0]))
        else:
            print(f'\nHere are the first {len(composites)} composite numbers greater than or equal to {minimum}:')
            print(str(composites)[1:-1])
            if yes_or_no('\nWould you like to see their prime factors? (Y or N)? '):
                print()
                for composite in composites: print(factorize(composite))
        repeat = yes_or_no('\nWould you like to enter a new set of numbers? (Y or N)? ')

# Declaration of Variables
done = False
user_choice = None

# Display info about the program, prime numbers, and composite numbers
print('')
print('┌─────────────────────────────────────────────────────────────────────────────────────┐')
print('│ Prime and Composite Number Finder                                                   │')
print('│ By The Prime Factors: Isa Mancuso, Ali Nur, Zabir Saif, Nathan Scrivens, Bob Wilson │')
print('├─────────────────────────────────────────────────────────────────────────────────────┤')
print('│ A prime number is an integer greater than 1 that is only divisible by 1 and itself. │')
print('│ A composite number is an integer greater than 1 that is not a prime number.         │')
print('└─────────────────────────────────────────────────────────────────────────────────────┘')

# Main Loop
while not done:
    print()
    print('┌───────────────────────────────────────────────────────┐')
    print('│ What would you like me to do?                         │')
    print('├───────────────────────────────────────────────────────┤')
    print('│ 1) Find all prime numbers within a certain range      │')
    print('│ 2) Generate an exact amount of prime numbers          │')
    print('│ 3) Find all composite numbers within a certain range  │')
    print('│ 4) Generate an exact amount of composite numbers      │')
    print('│ 5) Open wikipedia webpage about prime numbers         │')
    print('│ 6) Quit                                               │')
    print('└───────────────────────────────────────────────────────┘')
    print()
    user_choice = None
    while user_choice == None:
        user_choice = input('Please choose an option 1, 2, 3, 4, 5, or 6: ')
        if user_choice not in ['1','2','3','4','5','6'] : user_choice = None
    match user_choice:
        case '1': primes_in_range()
        case '2': generate_primes()
        case '3': composites_in_range()
        case '4': generate_composites()
        case '5': webbrowser.open('https://en.wikipedia.org/wiki/Prime_number')
        case '6': done = True
print()           
