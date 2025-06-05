import random

def generate_random_number(start=1, end=100):
    return random.randint(start, end)

if __name__ == "__main__":
    number = generate_random_number()
    print(f"Random Number between 1 and 100: {number}")
