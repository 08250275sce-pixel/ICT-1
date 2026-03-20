# Input marks for 3 subjects
math = float(input("Enter Math marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))

# Calculate total and percentage
total = math + science + english
percentage = (total / 300) * 100

print("\nTotal Marks:", total)
print("Percentage:", percentage)

# Determine grade using logical operators
if percentage >= 90 and math >= 90 and science >= 90 and english >= 90:
    grade = "A+ (Excellent!)"
elif percentage >= 80 and math >= 80 and science >= 80 and english >= 80:
    grade = "A (Very Good!)"
elif percentage >= 70 and math >= 70 and science >= 70 and english >= 70:
    grade = "B (Good!)"
elif percentage >= 60 and math >= 60 and science >= 60 and english >= 60:
    grade = "C (Average!)"
else:
    grade = "F (Needs Improvement!)"

print("Grade:", grade)

# Pass/Fail check using logical operators
if percentage >= 50 and math >= 35 and science >= 35 and english >= 35:
    print("Status: Passed ✅")
else:
    print("Status: Failed ❌")

# Remark for special cases using OR
if math < 35 or science < 35 or english < 35:
    print("Note: You failed in at least one subject!")