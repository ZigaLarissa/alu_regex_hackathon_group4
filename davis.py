import re

isbn_pattern = re.compile(r"^ISBN \d{3}.\d.\d{3}.\d{5}.\d$")

isbn_number = input("Test, eg: ISBN 638-0-862-84512-7")

match = isbn_pattern.match(isbn_number)

if match:
    print("Valid ISBN number.")
else:
    print("Invalid ISBN number.")