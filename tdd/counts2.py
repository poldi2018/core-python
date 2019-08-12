def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])

print(count_upper_case("Hello World"))