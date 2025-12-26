"""
ROLE: You are the 'Brain Coach'. You decide if a student knows a card well.
FUNCTION: calculate_knowledge_level(current_level, user_score)
INPUT: Current level (int) and a Score from 1 to 5 (int).
OUTPUT: Returns an updated level (int).

IMPLEMENTATION HINTS:
1. If the score is 5 (Easy), increase the level by 1.
2. If the score is 1 (Hard), reset the level to 0.

SKILL CHECK (Must include):
- List: Store the history of previous scores.
- Dictionary: Map level numbers to status strings (e.g., 0: "Newbie", 3: "Master").
- Tuple: Fixed score range (1, 2, 3, 4, 5).
- Logic: Nested 'if' statements to handle different score outcomes.
"""