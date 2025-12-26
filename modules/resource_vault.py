"""
ROLE: You are the 'Librarian'. You find study links for subjects.
FUNCTION: find_resources(subject_name)
INPUT: String (e.g., "Math").
OUTPUT: Returns a LIST of links or book names.

IMPLEMENTATION HINTS:
1. Create a large Dictionary where keys are Subjects and values are Lists of books.
2. Check if the subject exists in your dictionary.

SKILL CHECK (Must include):
- Dictionary: { "Math": ["Algebra 1", "Geometry PDF"], "History": ["WW2 Notes"] }
- List: The values inside the dictionary.
- Set: To keep track of "Already Opened" subjects.
- Logic: Use 'if subject in my_dict' to avoid errors.
"""