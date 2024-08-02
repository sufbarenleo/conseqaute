# Two dicts of node relationships
dict1 = {'node1': ['node2', 'node3'], 'node2': ['node3']}
dict2 = {'node1': ['node4'], 'node3': ['node5']}

# Merge the two dicts
merged_dict = dict1.copy()
for key, value in dict2.items():
    if key in merged_dict:
        merged_dict[key].extend(value)
    else:
        merged_dict[key] = value

print(merged_dict)
