#!/usr/bin/env python3
"""
Hello World Script for Data Science Pre-Course

This is a simple script to demonstrate basic Python concepts.
Students can use this to practice running Python scripts and
understanding basic programming concepts.
"""

def greet_student(name="Student"):
    """
    Simple function to greet a student
    
    Args:
        name (str): Name of the student (default: "Student")
    
    Returns:
        str: Greeting message
    """
    return f"Hello, {name}! Welcome to the Data Science Masters Pre-Course!"

def calculate_basic_stats(numbers):
    """
    Calculate basic statistics for a list of numbers
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        dict: Dictionary containing basic statistics
    """
    if not numbers:
        return {"error": "Empty list provided"}
    
    stats = {
        "count": len(numbers),
        "sum": sum(numbers),
        "mean": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }
    return stats

def main():
    """Main function to demonstrate the script functionality"""
    print("=" * 50)
    print("DATA SCIENCE PRE-COURSE - HELLO WORLD SCRIPT")
    print("=" * 50)
    
    # Greet the user
    name = input("Please enter your name (or press Enter for default): ").strip()
    if not name:
        name = "Student"
    
    greeting = greet_student(name)
    print(f"\n{greeting}\n")
    
    # Demonstrate basic statistics
    sample_numbers = [1, 2, 3, 4, 5, 10, 15, 20]
    print("Sample calculation with numbers:", sample_numbers)
    stats = calculate_basic_stats(sample_numbers)
    
    print("\nBasic Statistics:")
    for key, value in stats.items():
        print(f"  {key.capitalize()}: {value}")
    
    print("\n" + "=" * 50)
    print("Script completed successfully!")
    print("Try modifying this script to practice your Python skills!")
    print("=" * 50)

if __name__ == "__main__":
    main()