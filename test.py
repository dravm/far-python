def count_unique_names(name_list):
    unique_names = set()

    for names in name_list:
        for name in names.split(";"):
            unique_names.add(name.strip().lower())

    return len(unique_names)

# Example usage:
names_list = ["jeremy katz; gilad mor hayim", "Jeremy Katz", "doris pitilon; gilad mor hayim", "Doris Pitilon; Jeremy Katz"]
result = count_unique_names(names_list)
print(result)  # Output: 3
