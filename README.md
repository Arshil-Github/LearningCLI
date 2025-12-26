# LearningCLI: Modular Workflow & Memory CLI

LearningCLI is a terminal-based system designed to integrate task management, temporal validation, and spaced-repetition learning. The system is built on a modular architecture, consisting of an orchestrator hub and eight specialized logic engines.

The system operates by capturing user-defined academic/professional data, validating it through secondary logic modules, and processing it via algorithmic engines to determine task urgency and knowledge retention levels. All data is managed in-memory during the session and passed between modules via structured collections.

---

## Data Objects & Purpose

The system revolves around four primary data objects. Each person's script will focus on creating, validating, or processing these objects.

| Object       | Data Structure | Purpose                                                                        |
| ------------ | -------------- | ------------------------------------------------------------------------------ |
| Task         | Dictionary     | Stores `{name: str, subject: str, deadline: str, priority: int, status: bool}` |
| Flashcard    | Dictionary     | Stores `{front: str, back: str, mastery_level: int, category: str}`            |
| Grade Record | Dictionary     | Stores `{subject: str, score: float, weight: float}`                           |
| Resource     | Dictionary     | Stores `{title: str, type: str, location: str}`                                |

---

## System Logic Flow

- **Input**: Modules 1, 3, 6, and 7 collect user data.
- **Processing**: Modules 2, 4, 5, and 8 perform calculations, validations, and sorting on that data.
- **Integration**: Module 9 (The Hub) imports all other modules and manages the "Global Session State."

---

## Folder Structure

To maintain professional standards, the project should follow this structure. Each developer works on one file inside the `modules/` folder.

```
LearningCLI/
├── main.py
├── modules/
│   ├── task_manager.py
│   ├── date_engine.py
│   ├── anki_creator.py
│   ├── spaced_rep.py
│   ├── pomo_timer.py
│   ├── grade_analyst.py
│   ├── resource_vault.py
│   └── priority_sorter.py
├── README.md
└── .gitignore
```

---

## Module Specifications

### 1. `task_manager.py` (Task Registry)

Captures and initializes task data. It prompts for task identifiers and associated subjects.

- **Core Logic**: Iterative input collection to populate a List of Dictionaries.
- **Data Handling**: Uses a Set to extract and display unique subjects from the registry.

### 2. `date_engine.py` (Validation Engine)

Provides verification for temporal data. It parses string-based dates to ensure they conform to calendar logic.

- **Core Logic**: Uses a Dictionary mapping month indices to day counts to validate user-provided strings (e.g., "DD/MM").
- **Data Handling**: Implements Tuple-based constant storage for month names and error handling via Boolean flags.

### 3. `anki_creator.py` (Flashcard Architect)

Facilitates the creation of Question/Answer pairs for study cycles.

- **Core Logic**: Maps prompts to responses within a Dictionary structure.
- **Data Handling**: Stores the total deck in a List and categorizes entries using Sets based on user-defined labels.

### 4. `spaced_rep.py` (Algorithm Engine)

Calculates knowledge retention based on spaced-repetition principles.

- **Core Logic**: Increments or decrements a "Mastery Level" integer based on user performance scores.
- **Data Handling**: Uses a Dictionary to map mastery levels to specific review intervals.

### 5. `pomo_timer.py` (Session Scheduler)

Constructs interval-based study plans (Pomodoro technique).

- **Core Logic**: Generates a sequence of work and rest segments based on a set number of rounds.
- **Data Handling**: Uses a Tuple to define standard durations (25, 5) and a Dictionary to return the total projected session time.

### 6. `grade_analyst.py` (Statistical Engine)

Processes numeric performance data to generate categorical reports.

- **Core Logic**: Iterates through numeric Lists to calculate averages and determine letter grades via conditional mapping.
- **Data Handling**: Returns a Dictionary containing the average (Float) and the final evaluation (String).

### 7. `resource_vault.py` (Information Indexer)

Acts as a searchable repository for local reference materials.

- **Core Logic**: Filters a Dictionary of subjects and their associated reference Lists based on user queries.
- **Data Handling**: Uses a Set to track and return resources for unique subjects while ignoring duplicates.

### 8. `priority_sorter.py` (Heuristic Ranker)

Reorganizes task collections based on urgency and priority weights.

- **Core Logic**: Implements a sorting algorithm that buckets tasks into List-based tiers (High, Medium, Low).
- **Data Handling**: Uses a Dictionary of weight values to calculate a priority score for each task object.

### 9. `main.py` (System Orchestrator)

The entry point of the application. It manages the global session state and user interface.

- **Core Logic**: Imports all sub-modules and routes user input to the specific module functions via an infinite loop.
- **Data Handling**: Maintains the master Dictionary containing all tasks, cards, and grade logs generated during the session.

---

## Integration and Testing Syntax

All modules must be executable independently for verification. The following syntax is required at the end of every feature script:

```python
def module_main_function():
    # Primary logic here
    pass

if __name__ == "__main__":
    # Internal Test Sequence
    print("Executing Local Module Test...")
    # Mock data for verification
    test_data = {"key": "value"}
    print(f"Output Verification: {module_main_function(test_data)}")
```

---

## Git Implementation Workflow

To maintain repository integrity, all changes must be pushed via terminal using the following protocol:

1. **Directory Navigation**: `cd LearningCLI/modules`
2. **Staging**: `git add <filename>.py`
3. **Commitment**: `git commit -m "Feature: Implement [Module Name] with required data structures"`
4. **Synchronization**: `git push`

---

## Installation and Execution

1. Clone the repository to the local environment:

```bash
   git clone https://github.com/yourusername/LearningCLI.git
```

2. Navigate to the root directory:

```bash
   cd LearningCLI
```

3. Execute the orchestrator:

```bash
   python main.py
```
