#Write a function validate_data(data) that checks if a list of dictionaries 
#(e.g., [{"name": "Alice", "age": 30}, {"name": "Bob", "age": "25"}]) contains valid integer values for the "age" key. Return a list of invalid entries.

def validate_data(data):
    invalid_entries = []
    for entry in data:
        if 'age' not in entry or not isinstance(entry['age'], int):
            invalid_entries.append(entry)
    return invalid_entries
