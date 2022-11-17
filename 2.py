sample_dict = {
    "name": "Kelly",
    "surname": "Jones",
    "age": 3,
    "salary": 8000,
    "city": "Baszkirtystan"}

for k, v in sample_dict.items():
    print(f'{k:<8} = {v:>8}')

list = ["name", "age"]
D = {}

for k in list:
    if k in sample_dict.keys():
        D[k] = sample_dict[k]

print(D)