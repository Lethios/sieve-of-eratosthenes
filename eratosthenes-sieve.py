import sys

HELP_MESSAGE = f"""
Usage: python {sys.argv[0]} <command>

Available commands:
    help                 - Displays this help message.
    <positive_integer>   - The upper bound upto which prime numbers are generated.
"""

if sys.argv[1] == "help":
    print(HELP_MESSAGE)
    sys.exit(0)

elif sys.argv[1].isdigit():
    limit = int(sys.argv[1])

    prime_bool_list = [True] * (limit + 1)
    prime_list = []

    prime_bool_list[0], prime_bool_list[1] = False, False

    for number, prime in enumerate(prime_bool_list):
        if prime:
            prime_list.append(number)

            for i in range(number * 2, limit + 1, number):
                prime_bool_list[i] = False

    print(prime_list)
    sys.exit(0)

else:
    print("Enter a valid integer.")
    sys.exit(1)
