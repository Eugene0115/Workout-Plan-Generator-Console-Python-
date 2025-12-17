# Workout Plan Generator

![Python](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Console-based Python workout plan generator for educational purposes.
The program collects user input, allows workout generation by weekday or muscle group, applies a fixed strength training scheme (12 / 10 / 8 / 6), and includes a simple cardio mode. Built using core Python only, without external libraries or data persistence, with focus on clean control flow and input validation.

---

## Features
* User input validation (gender, age, weight, goal)
* Workout generation by weekday or muscle group
* Difficulty levels: light / medium / heavy
* Fixed strength training scheme: 4 sets (12 / 10 / 8 / 6)
* Simple cardio workout mode
* Random exercise selection without repetitions
* Warm-up and cool-down included
* Infinite loop menu until manual exit

---

## Requirements
* Python 3.x
* No external libraries

---

## Installation and Run
Clone the repository:
```bash
git clone https://github.com/your-username/workout-plan-generator.git
cd workout-plan-generator
```

Run the script:
```bash
python workout_planner.py
```

---

## Usage
1. Enter personal data:
   * gender
   * age
   * weight
   * goal (fat loss or muscle gain)
2. Choose workout mode:
   * by weekday
   * by muscle group
3. Select difficulty level:
   * light
   * medium
   * heavy
4. Review the generated workout
5. Press Enter to return to the main menu

The program continues running until `exit` or `q` is selected.

---

## Example Output

```bash
Muscle group: Shoulders
Difficulty: Heavy

Warm-up:
Cardio 5 minutes

Exercises:
Dumbbell Lateral Raises
4 sets: 12 / 10 / 8 / 6
Face Pull
4 sets: 12 / 10 / 8 / 6
Arnold Press
4 sets: 12 / 10 / 8 / 6
Cable Lateral Raises
4 sets: 12 / 10 / 8 / 6
Upright Barbell Row
4 sets: 12 / 10 / 8 / 6
```

---

## Weekly Muscle Group Split
- Monday — Chest
- Tuesday — Back
- Wednesday — Shoulders
- Thursday — Legs (quadriceps)
- Friday — Legs (posterior chain)
- Saturday — Biceps + Triceps
- Sunday — Cardio

---

## Difficulty Levels
- Light — 3 exercises
- Medium — 4 exercises
- Heavy — 5 exercises

---

## Project Structure
- `exercise_catalog` — dictionary of exercises grouped by muscle group
- `level_map` — difficulty levels mapped to exercise count
- `choose_level()` — handles difficulty selection
- `show_workout()` — unified workout output logic (strength and cardio)
- Main loop — menu navigation and program flow

---

## Design Decisions
- Functions are used instead of classes to keep the project simple and focused on core logic
- A unified workout generation function is used for both selection modes
- Dictionaries are used to map muscle groups, difficulty levels, and exercises
- Input validation is handled with loops instead of exceptions for clarity

---

## Limitations
- No data persistence
- Single-user mode
- Console interface only
- Educational project scope

---

## Future Improvements
- Save workout history to a file
- Add user profiles
- Extend exercise database
- Add rest time recommendations between sets

---
## License
This project is licensed under the MIT License.
