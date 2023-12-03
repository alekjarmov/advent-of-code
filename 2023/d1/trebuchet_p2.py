import re

sum = 0
valid_digits = ["zero", "one", "two", "three", "four", "five",
                "six", "seven", "eight", "nine", "0", "1", "2",
                "3", "4", "5", "6", "7", "8", "9"]
mapper = {"one": "1",
          "two": "2",
          "three": "3",
          "four": "4",
          "five": "5",
          "six": "6",
          "seven": "7",
          "eight": "8",
          "nine": "9",
          "zero": "0"}

valid_digits_string = f"({'|'.join(valid_digits)})"
dont_capture = f"(?!{valid_digits_string})"
first_digit_regex = f"{dont_capture}*{valid_digits_string}"
last_digit_regex = f".*{valid_digits_string}{dont_capture}*"
print(last_digit_regex)
for line in open("input.txt"):
    first = re.search(first_digit_regex, line).group(2)
    last = re.search(last_digit_regex, line).group(1)

    print(line, first, last)
    if first in mapper:
        first = mapper[first]
    if last in mapper:
        last = mapper[last]

    num = int(f'{first}{last}')
    sum += num

print(sum)
