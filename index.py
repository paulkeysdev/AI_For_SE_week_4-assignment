people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]


def ai_suggested_sort(data, key):
    return sorted(data, key=lambda x: x[key])


def manual_sort(data, key):
    sorted_data = data.copy()
    n = len(sorted_data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_data[j][key] > sorted_data[j + 1][key]:
                sorted_data[j], sorted_data[j +
                                            1] = sorted_data[j + 1], sorted_data[j]
    return sorted_data


def sort_people(data, key):
    return sorted(data, key=lambda x: x[key])


# Sample data
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Manual sort
print(manual_sort(people, "age"))

# AI suggested sort
print(ai_suggested_sort(people, "age"))
