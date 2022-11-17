sample_dict = {
    "name": "Kelly",
    "surname": "Jones",
    "age": 3,
    "salary": 8000,
    "city": "Baszkirtystan"}

for k, v in sample_dict.items():
    print(f'{k:<8} = {v:>8}')

D = {}

L = ["name", "age"]
for k in L:
    if k in sample_dict.keys():
        D[k] = sample_dict[k]

print(D)

L = ["name", "age"]
# for k in L:
#     if k in sample_dict.keys:
#         sample_dict.pop(k)

for k in L:
    sample_dict.pop(k, None)
print(sample_dict)