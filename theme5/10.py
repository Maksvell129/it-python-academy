items = [5, 2, 8, 5, 1, 2, 9, 5]
positions = {}

for index, value in enumerate(items, start=0):

    if value not in positions.keys():
        positions[value] = []

    positions[value].append(index)

print(positions)

for value, indexes in positions.items():
    if len(indexes) > 1:
        print(f"{value} находится на позициях {indexes}")



# for number in items:
#     duplicates = []
#
#     for i, value in enumerate(items):
#
#         if number == value:
#             duplicates.append(i)
#
#     if len(duplicates) > 1:
#         print(f"{number} находится на позициях {duplicates}")