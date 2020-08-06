"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
q = set(range(1, 70))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


# Your code here
counter = 0
addition = []
subtraction = []
for i in q:
    for j in q:
        addition.append(f(i)+f(j))
        subtraction.append(f(i) - f(j))


for i in addition:
    for j in subtraction:
        if i == j:
            counter += 1

print(counter)
