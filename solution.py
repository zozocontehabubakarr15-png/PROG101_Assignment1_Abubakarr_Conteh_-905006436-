# Course: PROG101 — Principles of Programming Logic and Design
# Student Name: Abubakarr Conteh
# Student ID: 905006436
# Project Title: Student Grade & Performance Tracker

def calculate_student_performance():
    print("=== Student Grade & Performance Tracker ===")
    try:
        # Accept student name and three assessment scores
        student_name = input("Enter student name: ").strip()
        if not student_name:
            student_name = "Student"
            
        score1 = float(input("Enter score for Assessment 1 (0-100): "))
        score2 = float(input("Enter score for Assessment 2 (0-100): "))
        score3 = float(input("Enter score for Assessment 3 (0-100): "))
        
        # Validate score ranges
        for i, score in enumerate([score1, score2, score3], start=1):
            if not (0 <= score <= 100):
                print(f"Warning: Score {i} ({score}) is outside the standard 0-100 range.")
        
        # Calculate average
        total_score = score1 + score2 + score3
        average_score = total_score / 3
        
        # Determine pass/fail status (threshold: 50.0)
        if average_score >= 50.0:
            status = "Pass"
        else:
            status = "Fail"
        
        # Display Summary Report
        print("\n" + "="*30)
        print("--- Academic Summary Report ---")
        print("="*30)
        print(f"Student Name : {student_name}")
        print(f"Assessment 1 : {score1}")
        print(f"Assessment 2 : {score2}")
        print(f"Assessment 3 : {score3}")
        print(f"Final Average: {average_score:.2f}")
        print(f"Status       : {status}")
        print("="*30)
        
    except ValueError:
        print("\nError: Please enter valid numerical values for the test scores.")

if __name__ == "__main__":
    calculate_student_performance()
