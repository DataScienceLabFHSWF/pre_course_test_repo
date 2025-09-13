#!/usr/bin/env python3
"""
Simple Data Analysis Script for Data Science Pre-Course

This script demonstrates basic data manipulation concepts that are
fundamental in data science. Students can use this to practice
working with lists, dictionaries, and simple data analysis.
"""

def create_sample_dataset():
    """
    Create a simple dataset for analysis
    
    Returns:
        list: List of dictionaries representing student records
    """
    students = [
        {"name": "Alice", "age": 22, "math_score": 85, "science_score": 90},
        {"name": "Bob", "age": 23, "math_score": 78, "science_score": 82},
        {"name": "Charlie", "age": 21, "math_score": 92, "science_score": 88},
        {"name": "Diana", "age": 24, "math_score": 76, "science_score": 94},
        {"name": "Eve", "age": 22, "math_score": 89, "science_score": 87},
    ]
    return students

def analyze_scores(students, subject):
    """
    Analyze scores for a specific subject
    
    Args:
        students (list): List of student dictionaries
        subject (str): Subject to analyze ("math_score" or "science_score")
    
    Returns:
        dict: Analysis results
    """
    scores = [student[subject] for student in students]
    
    analysis = {
        "subject": subject.replace("_score", "").title(),
        "total_students": len(students),
        "average_score": round(sum(scores) / len(scores), 2),
        "highest_score": max(scores),
        "lowest_score": min(scores),
        "passing_students": len([score for score in scores if score >= 80])
    }
    
    return analysis

def find_top_performer(students):
    """
    Find the student with the highest average score
    
    Args:
        students (list): List of student dictionaries
    
    Returns:
        dict: Top performing student with average score
    """
    top_student = None
    highest_avg = 0
    
    for student in students:
        avg_score = (student["math_score"] + student["science_score"]) / 2
        if avg_score > highest_avg:
            highest_avg = avg_score
            top_student = student.copy()
            top_student["average_score"] = round(avg_score, 2)
    
    return top_student

def display_analysis_results(students):
    """
    Display comprehensive analysis results
    
    Args:
        students (list): List of student dictionaries
    """
    print("STUDENT PERFORMANCE ANALYSIS")
    print("=" * 40)
    
    # Display all students
    print("\nAll Students:")
    for student in students:
        avg = (student["math_score"] + student["science_score"]) / 2
        print(f"  {student['name']}: Math={student['math_score']}, "
              f"Science={student['science_score']}, Average={avg:.1f}")
    
    # Analyze each subject
    print("\nSubject Analysis:")
    for subject in ["math_score", "science_score"]:
        analysis = analyze_scores(students, subject)
        print(f"\n{analysis['subject']}:")
        print(f"  Average Score: {analysis['average_score']}")
        print(f"  Highest Score: {analysis['highest_score']}")
        print(f"  Lowest Score: {analysis['lowest_score']}")
        print(f"  Students Passing (≥80): {analysis['passing_students']}/{analysis['total_students']}")
    
    # Find top performer
    top_student = find_top_performer(students)
    print(f"\nTop Performer: {top_student['name']} with average score of {top_student['average_score']}")

def main():
    """Main function to run the data analysis"""
    print("DATA SCIENCE PRE-COURSE - SIMPLE DATA ANALYSIS")
    print("=" * 50)
    
    # Create and analyze sample dataset
    students = create_sample_dataset()
    display_analysis_results(students)
    
    print("\n" + "=" * 50)
    print("Analysis completed!")
    print("Try modifying the dataset or adding new analysis functions!")
    print("=" * 50)

if __name__ == "__main__":
    main()