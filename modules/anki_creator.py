"""
ROLE: You are the 'Note Taker'. You help students make study cards.
FUNCTION: create_flashcards()
INPUT: User keyboard input (Question and Answer).
OUTPUT: Returns a LIST of DICTIONARIES.
        Example: [{"Q": "2+2", "A": "4"}, {"Q": "Capital of France", "A": "Paris"}]

IMPLEMENTATION HINTS:
1. Use a loop to let the user create as many cards as they want.
2. Use string methods like .upper() or .lower() to keep things neat.

SKILL CHECK (Must include):
- Dictionary: To link one Question to one Answer.
- List: To store the stack of cards.
- Set: To store unique 'Tags' (like #science, #history).
- Logic: If input is empty, don't save the card.
"""