# Sort a list of dictionaries by a given key in Python

# Original incomplete function
def sort_dicts_by_key(data, key):
    # Copilot/Tabnine suggestion here
    pass

# Completed function with documentation
def sort_dicts_by_key(data, key):
    """
    Sorts a list of dictionaries by a specified key.
    
    :param data: List[Dict] - A list of dictionaries
    :param key: str - The key to sort the dictionaries by
    :return: List[Dict] - Sorted list of dictionaries
    """
    return sorted(data, key=lambda x: x.get(key, None))

# Example usage
if __name__ == "__main__":
    # Test data
    students = [
        {"name": "Alice", "age": 25, "grade": 88},
        {"name": "Bob", "age": 22, "grade": 92},
        {"name": "Charlie", "age": 24, "grade": 85},
        {"name": "Diana", "age": 23, "grade": 95}
    ]
    
    # Sort by age
    sorted_by_age = sort_dicts_by_key(students, "age")
    print("Sorted by age:", sorted_by_age)
    
    # Sort by grade
    sorted_by_grade = sort_dicts_by_key(students, "grade")
    print("Sorted by grade:", sorted_by_grade)
    
    # Sort by non-existent key
    sorted_by_invalid = sort_dicts_by_key(students, "invalid_key")
    print("Sorted by invalid key:", sorted_by_invalid)