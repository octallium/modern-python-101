"""

Dictionary:
-----------

Louis has given his exams and received marks. Let's check
out how did he fare.

Dictionary makes it easy to have key-value pairs.

Info:
-----
Lookups are very fast!!!
"""

marks: dict[str, int] = {
    "Math": 80,
    "Science": 82,
    "History": 78,
    "English": 35,
    "Python": 98,
    "Physics": 63,
}
print(f"Marks: {marks}")

# ---------------------------------------------------------------------
# Louis wants to check out all the subjects (Keys)
# ---------------------------------------------------------------------

for subject in marks.keys():
    print(subject)

# ---------------------------------------------------------------------
# Louis wants to check out all the marks (Values)
# ---------------------------------------------------------------------

for score in marks.values():
    print(score)

# ---------------------------------------------------------------------
# Louis wants to check out all the subjects & marks together (Key-Value)
# ---------------------------------------------------------------------

for subject, score in marks.items():
    print(f"{subject}: {score}/100")

# ----------------------------------------------------------------------
# Louis wants to check if he passed all of the subjects, Passing mark 50
# ----------------------------------------------------------------------

for subject, score in marks.items():
    if score >= 50:
        print(f"{subject}: PASS")
    else:
        print(f"{subject}: FAILED!!!")

# ----------------------------------------------------------------------
# Louis requests revaluation of his English paper, there was a totalling
# mistake and right marks are 70
# ----------------------------------------------------------------------

marks["English"] = 70
print(f"Louis scored {marks['English']} in English.")

# ----------------------------------------------------------------------
# Louis also took Geography and scored 78
# ----------------------------------------------------------------------

marks["Geography"] = 78

# ----------------------------------------------------------------------
# Louis again wants to check if he passed in all of the subjects
# ----------------------------------------------------------------------

for subject, score in marks.items():
    if score >= 50:
        print(f"{subject}: PASS")
    else:
        print(f"{subject}: FAILED!!!")

# ----------------------------------------------------------------------
# Friends on Zortan want's to know how much Louis scored in Python
# ----------------------------------------------------------------------

# Alternative 1
# --------------
python_score = marks["Python"]
print(f"Louis scored {python_score} in Python")

# Alternative 2
# --------------
python_score = marks.get("Python")
print(f"Louis scored {python_score} in Python")

# ----------------------------------------------------------------------
# Friends on Earth want's to know how much Louis scored in Java
# ----------------------------------------------------------------------

# Alternative 1 - Will throw an error
# -----------------------------------
# java_score = marks["Java"]
# print(f"Louis scored {java_score} in java")

# Alternative 2 - Preferred Approach
# ----------------------------------
java_score: int | None = marks.get("Java")

if java_score is None:
    print("Louis did not study Java")
else:
    print(f"Louis scored {java_score} in java")

# -----------------------------------
# Deleting an element from dictionary
# -----------------------------------

del marks["English"]

print(f"Marks: {marks}")
