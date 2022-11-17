int_values = [10, 20, 33]
str_keys = ["Ten", "Twenty", "Thirty"]

dictionary0 = dict(zip(str_keys, int_values))
dictionary1 = {}

for i in range(len(int_values)):
    dictionary1[str_keys[i]] = int_values[i]

dictionary2 = {
    "Thirty":30,
    "Fourty":40,
    "Fifty":50
}

dictionary3 = dictionary1.copy()
dictionary3.update(dictionary2)

print(dictionary3)