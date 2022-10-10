import json

lower = 48
upper = 57
dash = 45

class Json:
    def __init__(self, s):
        self.parsed = json.loads(s)



def count_numbers(s):
    numbers = []
    current = ""

    for c in s:
        ch = ord(c)
        if (ch >= lower and ch <= upper) or ch == dash:
            current += c
        else:
            numbers.append(current)
            current = ""

    return sum([int(n) for n in numbers if n != ""])

# def remove_red(s, start, finish):
# define recursive function that enters func on [ or {, and exits and returns on ], } -> ] with red means include in count, } with red means exclude in count



with open("input.txt") as f:
    input = f.read().strip()

p1 = count_numbers(input)

print("Part 1:", p1)

j = Json(input)

print(j.parsed)
