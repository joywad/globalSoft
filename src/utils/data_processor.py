import numpy as np
import pandas as pd
from typing import List, Dict, Union, Any

class DataProcessor:
    """A utility class for processing various types of data."""
    
    @staticmethod
    def calculate_statistics(data: List[float]) -> Dict[str, float]:
        """Calculate basic statistics for a list of numbers."""
        if not data:
            return {
                "mean": 0,
                "median": 0,
                "std": 0,
                "min": 0,
                "max": 0
            }
        
        return {
            "mean": float(np.mean(data)),
            "median": float(np.median(data)),
            "std": float(np.std(data)),
            "min": float(np.min(data)),
            "max": float(np.max(data))
        }
    
    @staticmethod
    def clean_text_data(text: str) -> str:
        """Clean and normalize text data."""
        # Remove extra whitespace
        text = " ".join(text.split())
        # Convert to lowercase
        text = text.lower()
        return text
    
    @staticmethod
    def create_dataframe(data: List[Dict[str, Any]]) -> pd.DataFrame:
        """Create a pandas DataFrame from a list of dictionaries."""
        return pd.DataFrame(data)
    
    @staticmethod
    def filter_data(data: List[Dict[str, Any]], conditions: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Filter a list of dictionaries based on conditions."""
        filtered_data = []
        for item in data:
            matches = all(
                item.get(key) == value
                for key, value in conditions.items()
            )
            if matches:
                filtered_data.append(item)
        return filtered_data

# Example usage
if __name__ == "__main__":
    # Example numerical data
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    stats = DataProcessor.calculate_statistics(numbers)
    print("Statistics:", stats)
    
    # Example text data
    text = "  This   is   some   Sample   TEXT   "
    cleaned_text = DataProcessor.clean_text_data(text)
    print("Cleaned text:", cleaned_text)
    
    # Example structured data
    data = [
        {"name": "John", "age": 30, "city": "New York"},
        {"name": "Alice", "age": 25, "city": "Boston"},
        {"name": "Bob", "age": 35, "city": "New York"}
    ]
    
    # Create DataFrame
    df = DataProcessor.create_dataframe(data)
    print("\nDataFrame:")
    print(df)
    
    # Filter data
    filtered = DataProcessor.filter_data(data, {"city": "New York"})
    print("\nFiltered data (New York only):")
    print(filtered)