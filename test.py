import itertools

my_list = [1, 2, 3]
all_combinations = []

for r in range(len(my_list) + 1):  # Iterate from length 0 to full length
    for combo in itertools.combinations(my_list, r):
        all_combinations.append(list(combo))

print(all_combinations)