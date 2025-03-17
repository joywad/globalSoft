from utils.data_processor import DataProcessor
import random

def generate_sample_data(n: int = 100):
    """Generate sample data for demonstration."""
    return [random.uniform(0, 100) for _ in range(n)]

def main():
    # Generate sample data
    data = generate_sample_data()
    
    # Calculate statistics
    stats = DataProcessor.calculate_statistics(data)
    print("\n=== Data Statistics ===")
    for key, value in stats.items():
        print(f"{key.capitalize()}: {value:.2f}")
    
    # Example with text processing
    sample_texts = [
        "  This is   a   MESSY    text   ",
        "ANOTHER    example   OF    messy   TEXT   ",
        "  Final    EXAMPLE    here   "
    ]
    
    print("\n=== Text Cleaning Examples ===")
    for text in sample_texts:
        cleaned = DataProcessor.clean_text_data(text)
        print(f"Original: {text}")
        print(f"Cleaned : {cleaned}\n")
    
    # Example with structured data
    people = [
        {"name": "John", "age": 30, "city": "New York", "occupation": "Engineer"},
        {"name": "Alice", "age": 25, "city": "Boston", "occupation": "Designer"},
        {"name": "Bob", "age": 35, "city": "New York", "occupation": "Manager"},
        {"name": "Carol", "age": 28, "city": "Boston", "occupation": "Engineer"},
    ]
    
    print("=== Data Filtering Examples ===")
    # Filter engineers
    engineers = DataProcessor.filter_data(people, {"occupation": "Engineer"})
    print("\nEngineers:")
    for person in engineers:
        print(f"- {person['name']} from {person['city']}")
    
    # Filter people from New York
    new_yorkers = DataProcessor.filter_data(people, {"city": "New York"})
    print("\nPeople from New York:")
    for person in new_yorkers:
        print(f"- {person['name']}, {person['occupation']}")

if __name__ == "__main__":
    main()