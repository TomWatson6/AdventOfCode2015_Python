import itertools

class Ingredient:
    def __init__(self, s):
        parts = s.split(" ")
        self.name = parts[0].strip(":")
        self.capacity = int(parts[2].strip(","))
        self.durability = int(parts[4].strip(","))
        self.flavor = int(parts[6].strip(","))
        self.texture = int(parts[8].strip(","))
        self.calories = int(parts[10].strip(","))

    def cap_value(self, x):
        v = self.capacity * x
        return v

    def dur_value(self, x):
        v = self.durability * x
        return v

    def flavor_value(self, x):
        v = self.flavor * x
        return v

    def texture_value(self, x):
        v = self.texture * x
        return v

    def calorie_value(self, x):
        v = self.calories * x
        return v


with open("input.txt") as f:
    ingreds = [Ingredient(x) for x in f.readlines() if x != ""]

combos = []

for a in range(1, 100):
    for b in range(1, 100):
        for c in range(1, 100):
            for d in range(1, 100):
                if a + b + c + d == 100:
                    combos.append([a, b, c, d])

perms = {}

for c in combos:
    p = itertools.permutations(c)
    for p0 in p:
        perms[tuple(p0)] = True

perms = [list(x) for x in perms.keys()]

print("Generated {} perms to run through".format(len(perms)))

max_calories = 500
cal_highest = 0
highest = 0

for p in perms:
    v0 = ingreds[0].cap_value(p[0]) + ingreds[1].cap_value(p[1]) + ingreds[2].cap_value(p[2]) + ingreds[3].cap_value(p[3])
    v0 = v0 if v0 > 0 else 0
    v1 = ingreds[0].dur_value(p[0]) + ingreds[1].dur_value(p[1]) + ingreds[2].dur_value(p[2]) + ingreds[3].dur_value(p[3])
    v1 = v1 if v1 > 0 else 0
    v2 = ingreds[0].flavor_value(p[0]) + ingreds[1].flavor_value(p[1]) + ingreds[2].flavor_value(p[2]) + ingreds[3].flavor_value(p[3])
    v2 = v2 if v2 > 0 else 0
    v3 = ingreds[0].texture_value(p[0]) + ingreds[1].texture_value(p[1]) + ingreds[2].texture_value(p[2]) + ingreds[3].texture_value(p[3])
    v3 = v3 if v3 > 0 else 0
    v4 = ingreds[0].calorie_value(p[0]) + ingreds[1].calorie_value(p[1]) + ingreds[2].calorie_value(p[2]) + ingreds[3].calorie_value(p[3])
    v = v0 * v1 * v2 * v3
    highest = max(highest, v)
    if v4 == max_calories:
        cal_highest = max(cal_highest, v)

print("Part 1: {}".format(highest))
print("Part 2: {}".format(cal_highest))


