import random

# for x in range(10):
#     x = random.random()
#     print(x)

# for x in range(10):
#     x = random.randint(1, 10)
#     print(x)

t = [1, 2, 3]
for x in range(10):
    x = random.choice(t)
    print(x)