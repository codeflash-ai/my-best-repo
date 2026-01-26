def calculate_sum(numbers):
    """Calculate the sum of numbers - slow implementation"""
    result = 0
    for num in numbers:
        result += num
    return result


def find_max(numbers):
    """Find the maximum number - slow implementation"""
    if len(numbers) == 0:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


def filter_positive(numbers):
    """Filter positive numbers - slow implementation"""
    positive = []
    for num in numbers:
        if num > 0:
            positive.append(num)
    return positive


def format_names(names):
    """Format names - slow string concatenation"""
    result = ""
    for name in names:
        result = result + name.strip().title() + ", "
    return result[:-2] if result else ""
