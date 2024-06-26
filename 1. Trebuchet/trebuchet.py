import re

def  first_digit(input_string:str) -> str:
    '''
    Returns the first digit character in the given input string and excludes all other digits
    '''
    pattern:str = r"(?=^.*?(?P<first_digit>(\d)))"
    searches:re.Match = re.search(pattern, input_string)
    groups:str = searches.group("first_digit")
    return groups

def  last_digit(input_string:str) -> str:
    '''
    Returns the last digit character in the given input string and excludes all other digits
    '''
    pattern:str = r"(?P<last_digit>\d)(?!.*\d)"
    searches:re.Match = re.search(pattern, input_string)
    groups:str = searches.group("last_digit")
    return groups

def join_digits(*digits:str) -> int:
    '''
    Returns a string concatenation of any number of given digits as an integer value
    '''
    join:str = ""
    for digit in digits:
        join += digit

    to_integer = int(join)
    return to_integer

def sum_nums(*nums:int) -> int:
    '''
    Total of one or more given integer arguments
    '''
    total:int = 0
    for num in nums:
        total += num

    return total

def current_dir() -> str:
    '''
    Returns the current directory of __main__
    '''
    pattern:str = r"^.*[/\\]"
    searches:re.Match = re.search(pattern, __file__)
    groups:str = searches.group(0)
    return groups

def sub_words(input_string:str) -> str:
    '''
    Returns a string containing all occurences of digits in word and numerical formats
    All other characters are removed
    '''
    digits:dict = {
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9",
        }

    pattern:str = f"(?=({'|'.join((*digits.keys(), *digits.values()))}))"
    words:list[str] = re.findall(pattern, input_string)

    sub:list = []
    for word in words:
        if word in digits.keys():
            sub.append(digits[word])
        else:
            sub.append(word)

    return "".join(sub)

def answer(input_string:str) -> int:
    '''
    Returns full transformation of given input string
    '''
    words:str = sub_words(input_string)
    first:str = first_digit(words)
    last:str = last_digit(words)

    nums:int = join_digits(first, last)

    return nums

def _part_one() -> int:
    '''
    Solution to part one: 56397
    '''
    directory = current_dir()
    with open(f"{directory}calibrations", "r") as file_handle:
        lines:list[str] = file_handle.read().split("\n")

        first:tuplet[str] = (first_digit(digit) for digit in lines)
        last:tuplet[str] = (last_digit(digit) for digit in lines)
        nums:tuplet[int] = (join_digits(*digits) for digits in zip(first,last))

        return sum_nums(*nums)

def _part_two() -> int:
    '''
    Solution to part two: 55701
    '''
    directory = current_dir()
    with open(f"{directory}calibrations", "r") as file_handle:
        raw_lines = file_handle.read().split("\n")
        lines:list[str] = [sub_words(line) for line in raw_lines]
        nums = (answer(line) for line in lines)

        return sum_nums(*nums)

def main():
    print(_part_one())  # CORRECT: 56397
    print(_part_two())  # INCORRECT: expected 55701

if __name__ == "__main__":
    main()