"""
ROLE: You are the 'Security Guard'. You make sure dates entered are real.
FUNCTION: is_date_valid(date_string)
INPUT: A string like "15/05" (Day/Month).
OUTPUT: Returns True (if valid) or False (if fake).

IMPLEMENTATION HINTS:
1. Split the string by the "/" to get the Day and Month as integers.
2. Use a Dictionary where keys are month numbers (1-12) and values are days in that month.
3. Check: Is the month between 1-12? Is the day within the limit for that month?

SKILL CHECK (Must include):
- Dictionary: {1: 31, 2: 28, 3: 31...} for month lengths.
- Tuple: Store names of months ("Jan", "Feb"...) that cannot be changed.
- List: Store "Holiday" dates that are invalid for school.
- Logic: Use 'if/else' to return True or False.
"""