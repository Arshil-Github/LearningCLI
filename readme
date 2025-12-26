# LearningCLI: Modular Workflow & Memory CLI

LearningCLI is a terminal-based system designed to integrate task management, temporal validation, and spaced-repetition learning. The system is built on a modular architecture, consisting of an orchestrator hub and eight specialized logic engines.

The system operates by capturing user-defined academic/professional data, validating it through secondary logic modules, and processing it via algorithmic engines to determine task urgency and knowledge retention levels. All data is managed in-memory during the session and passed between modules via structured collections.

---

## Data Objects & Purpose

The system revolves around four primary data objects. Each person's script will focus on creating, validating, or processing these objects.

| Object | Data Structure | Purpose |
|--------|---------------|---------|
| Task | Dictionary | Stores `{name: str, subject: str, deadline: str, priority: int, status: bool}` |
| Flashcard | Dictionary | Stores `{front: str, back: str, mastery_level: int, category: str}` |
| Grade Record | Dictionary | Stores `{subject: str, score: float, weight: float}` |
| Resource | Dictionary | Stores `{title: str, type: str, location: str}` |

---

## System Logic Flow

- **Input**: Modules 1, 3, 6, and 7 collect user data.
- **Processing**: Modules 2, 4, 5, and 8 perform calculations, validations, and sorting on that data.
- **Integration**: Module 9 (The Hub) imports all other modules and manages the "Global Session State."

---

## Folder Structure

To maintain professional standards, the project should follow this structure. Each developer works on one file inside the `modules/` folder.