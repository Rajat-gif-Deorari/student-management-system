# Student Management System

A simple command-line Student Management System built with Python. It lets you add, view, search, update, and delete student records, while storing data locally in a JSON file.

## Features

- **Add students** with a roll number, name, and marks for three subjects.
- **Display student records** in a formatted table.
- **Search** for a student by roll number.
- **Update** a student's name and marks.
- **Delete** a student record by roll number.
- **Calculate average marks** when a student is added or updated.
- **Save data automatically** to `students.json` after adding, updating, or deleting records.
- **Load saved records** when the program starts.
- **Basic input error handling** for non-numeric roll numbers and marks.

## Requirements

- Python 3.8 or later (the project uses standard-library modules only).
- No third-party packages are required.

## Getting Started

1. Download or clone this project.
2. Open a terminal in the project directory.
3. Run the program:

   ```bash
   python project1.py
   ```

   On some systems, use:

   ```bash
   python3 project1.py
   ```

4. Follow the on-screen menu and enter the number for the operation you want.

## Menu Options

| Option | Action |
| --- | --- |
| 1 | Add a student |
| 2 | Display all students |
| 3 | Search for a student by roll number |
| 4 | Update a student's name and marks |
| 5 | Delete a student |
| 6 | Display student records |
| 7 | Exit the program |

**Note:** In the current implementation, option 6 displays the student records; it does not perform a separate average-only calculation. Average marks are calculated automatically when records are added or updated.

## Data Storage

Student records are saved in `students.json` in the current working directory. The file is created when a record is saved for the first time. Each record stores:

- `roll`: student's roll number
- `name`: student's name
- `marks`: marks for three subjects
- `average`: average of the three subject marks

Example record:

```json
{
  "roll": 101,
  "name": "Aarav",
  "marks": [85, 90, 78],
  "average": 84.33333333333333
}
```

If you remove `students.json`, previously saved records will no longer be available to the program.

## Concepts Used

- Python functions
- Lists and dictionaries
- Loops and conditional statements
- User input and type conversion
- Exception handling with `try` / `except`
- File handling
- JSON serialization and deserialization
- Basic arithmetic for average marks

## Current Limitations

- Exactly three subject marks are collected for each student.
- Marks are converted to numbers, but the program does not currently validate that they are between 0 and 100.
- Duplicate roll numbers are not prevented.
- Option 6 currently calls the display function rather than calculating or displaying averages separately.
- Choosing option 7 exits the program; records are already saved after add, update, and delete operations.

## Possible Improvements

- Validate that marks are between 0 and 100.
- Prevent duplicate roll numbers.
- Add a dedicated average-marks report.
- Allow a configurable number of subjects.
- Add sorting by roll number or average.
- Improve handling of missing or invalid JSON data.

## License

No license has been specified for this project.
