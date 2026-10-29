
unique_ids = {101, 102, 101, 103, 102}

print(unique_ids)

unique_ids.add(108)
unique_ids.add(99)
unique_ids.remove(101)
unique_ids.discard(101)
unique_ids.update({109, 111})
unique_ids.update({109, 111})

print(99 in unique_ids)