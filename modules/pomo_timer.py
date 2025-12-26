"""
ROLE: You are the 'Time Keeper'. You plan study sessions.
FUNCTION: get_timer_schedule(rounds)
INPUT: Number of rounds (int).
OUTPUT: Returns a LIST of strings.
        Example: ["Study", "Break", "Study", "Break"]

IMPLEMENTATION HINTS:
1. Each round is 1 Study block and 1 Break block.
2. Use a 'for' loop to repeat based on the 'rounds' input.

SKILL CHECK (Must include):
- List: To build the sequence of Study/Break.
- Tuple: Fixed times (25, 5) minutes.
- Dictionary: Track total minutes spent in each mode {"Study": 50, "Break": 10}.
- Logic: If rounds > 4, add a "Long Break" to the list.
"""