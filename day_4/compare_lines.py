def compare_lines(winning_numbers: list[str], numbers_you_have: list[str]) -> int:
    """
    Compares two lists of numbers and calculates the number of matches.

    Args:
        winning_numbers (List[str]): The list of winning numbers.
        numbers_you_have (List[str]): The list of numbers you possess.

    Returns:
        int: The total count of matching numbers between `winning_numbers` and `numbers_you_have`.
    """
    points = 0    
    for i in winning_numbers:
        if i in numbers_you_have:
           points += 1

    return points