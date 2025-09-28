import re


def check_strength(password: str) -> int:
    """Return a password strength score from 0 to 5 based on complexity."""
    length = len(password) >= 8
    lower = re.search(r'[a-z]', password) is not None
    upper = re.search(r'[A-Z]', password) is not None
    digit = re.search(r'\d', password) is not None
    special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    return sum([length, lower, upper, digit, special])


def main() -> None:
    pwd = input("Enter a password to evaluate: ")
    strength = check_strength(pwd)
    print(f"Password strength (0-5): {strength}")


if __name__ == "__main__":
    main()
