print("🎓 Grade Manager")
print("Enter grades between 0 and 20.")
print("Type 'exit' when you are finished.")

grades = []
passed = []
failed = []

while True:
    grade = input("Enter a grade: ")

    if grade == "exit":
        break

    grade = float(grade)

    if grade < 0 or grade > 20:
        print("Invalid grade!")
        continue

    grades.append(grade)

    if grade >= 12:
        print("Passed!")
        passed.append(grade)
    else:
        print("Failed!")
        failed.append(grade)

if len(grades) > 0:
    print("\n--- Results ---")
    print("Average:", sum(grades) / len(grades))
    print("Highest:", max(grades))
    print("Lowest:", min(grades))
    print("Passed:", passed)
    print("Failed:", failed)
else:
    print("No grades entered.")

