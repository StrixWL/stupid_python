import sys as sys


def get_user_prompt():
    """
    Prompt the user to input text from standard input.

    Returns:
        str: The text entered by the user.
    """
    user_input = ""
    print("What is the text to count?")
    user_input = sys.stdin.read()
    return user_input


def print_count(count):
    """
    Print a summary of character counts in the given text.

    Args:
        count (dict): A dictionary with keys 'total', 'upper', 'lower',
                      'punctuation', 'spaces', 'digits', representing counts.
    """
    print("The text contains", count['total'], "characters:")
    print(count['upper'], "upper letters")
    print(count['lower'], "lower letters")
    print(count['punctuation'], "punctuation marks")
    print(count['spaces'], "spaces")
    print(count['digits'], "digits")


def evaluate(s):
    """
    Analyze the input text and count the number of characters by type.

    Args:
        s (str): The string to evaluate.

    Counts:
        - total characters
        - uppercase letters
        - lowercase letters
        - punctuation marks
        - spaces
        - digits
    """
    count = {
        "total": len(s),
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "digits": 0,
        "spaces": 0,
    }
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for c in s:
        if c.isupper():
            count['upper'] += 1
        elif c.islower():
            count['lower'] += 1
        elif c in punctuation_chars:
            count['punctuation'] += 1
        elif c.isdigit():
            count['digits'] += 1
        elif c.isspace():
            count['spaces'] += 1
    print_count(count)


def main():
    """
    Main function to get text input (from command line or stdin)
    and evaluate its character composition.
    """
    user_input = ""
    if len(sys.argv) > 2:
        print(AssertionError("AssertionError: more than one\
 argument is provided"))
        exit(1)
    elif len(sys.argv) == 2:
        user_input = sys.argv[1]
    else:
        user_input = get_user_prompt()
    evaluate(user_input)


if (__name__ == "__main__"):
    try:
        main()
    except BaseException:
        exit(1)
