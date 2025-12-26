"""
ROLE: You are the 'Input Clerk'. You help students record their homework.
FUNCTION: add_task_session() 
INPUT: User keyboard input (Task name, Subject name).
OUTPUT: Returns a LIST of DICTIONARIES.
        Example: [{"name": "Lab 1", "subject": "Math"}, {"name": "Essay", "subject": "English"}]

IMPLEMENTATION HINTS:
1. Create an empty List to hold your tasks.
2. Use a 'while' loop. Ask: "Enter task name or 'exit' to stop".
3. Inside the loop, create a Dictionary for each task.
4. Add the Dictionary to your List.

SKILL CHECK (Must include):
- List: To store all tasks.
- Dictionary: To store individual task details.
- Set: Use a Set to store unique subjects (to avoid showing "Math" twice).
- Loops: 'while' loop for data entry.
- Conditionals: 'if' to check if user typed 'exit'.
"""