"""

Tuple:
------
Time for Louis to go to school, and its time for him to
choose subjects. School doesn't want students to change
subjects after they are chosen, so they use Tuple.

Tuple is like a stricter brother of List. Once a Tuple is
created, it cannot be edited.

Info:
-----
Tuple also start from index 0
"""

subjects: tuple[str, str, str] = ("Math", "Science", "History")
# ----------------------Index No (   0,       1,        2     )


# ---------------------------------------------------------------------
# Louis wants to count his subjects
# ---------------------------------------------------------------------

print(f"No. of subjects: {len(subjects)}")

# ---------------------------------------------------------------------
# Louis needs to signup for all the subjects
# ---------------------------------------------------------------------

for subject in subjects:
    print(f"Louis is signing up for: {subject}")

# ---------------------------------------------------------------------
# Louis wants to see which is his second subject
# ---------------------------------------------------------------------

print(subjects[1])
# -------------^ Remember since Tuple starts from index 0, we use 1 here

# ---------------------------------------------------------------------
# School wants Louis to take another 3 subjects to get full credits
# ---------------------------------------------------------------------

addl_subjects = ("English", "Python", "Physics")
total_subjects = subjects + addl_subjects
print(f"All subjects: {total_subjects}")

# ---------------------------------------------------------------------
# Louis loves Python, and wants to see if it's there in his subjects
# ---------------------------------------------------------------------

if "Python" in total_subjects:
    print("Yayy, Louis is going to learn Python!!")
else:
    print("Oh ho, no Python for Louis")
