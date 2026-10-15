import json
import os

FILENAME = "students.json"


def load_data():
  if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
      return json.load(f)
  return []


def save_data(students):
  with open(FILENAME, "w") as f:
    json.dump(students, f, indent=4)


def add_student(students):
  try:
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = []
    for i in range(3):
      m = float(input(f"Enter marks for subject {i+1} (out of 100): "))
      marks.append(m)
    avg = sum(marks) / len(marks)
    students.append(
        {"roll": roll, "name": name, "marks": marks, "average": avg}
    )
    save_data(students)
    print("Student added and saved successfully!")
  except ValueError:
    print("Invalid input. Please enter numeric values where required.")


def display_students(students):
  if not students:
    print("No student records found.")
    return
  print(f"{'Roll No':<10}{'Name':<20}{'Marks':<25}{'Average':<10}")
  print("-" * 65)
  for s in students:
    marks_str = ", ".join(map(str, s["marks"]))
    print(
        f"{s['roll']:<10}{s['name']:<20}{marks_str:<25}{s['average']:<10.2f}"
    )


def search_student(students):
  try:
    roll = int(input("Enter Roll Number to search: "))
    for s in students:
      if s["roll"] == roll:
        print("\nStudent Found:")
        print(f"Roll No: {s['roll']}")
        print(f"Name: {s['name']}")
        print(f"Marks: {s['marks']}")
        print(f"Average Marks: {s['average']:.2f}")
        return
    print("Student not found.")
  except ValueError:
    print("Invalid roll number.")


def update_student(students):
  try:
    roll = int(input("Enter Roll Number to update: "))
    for s in students:
      if s["roll"] == roll:
        s["name"] = input("Enter New Name: ")
        marks = []
        for i in range(3):
          m = float(input(f"Enter new marks for subject {i+1} (out of 100): "))
          marks.append(m)
        s["marks"] = marks
        s["average"] = sum(marks) / len(marks)
        save_data(students)
        print("Student record updated successfully!")
        return
    print("Student not found.")
  except ValueError:
    print("Invalid input.")


def delete_student(students):
  try:
    roll = int(input("Enter Roll Number to delete: "))
    for i, s in enumerate(students):
      if s["roll"] == roll:
        students.pop(i)
        save_data(students)
        print("Student record deleted successfully!")
        return
    print("Student not found.")
  except ValueError:
    print("Invalid roll number.")


def main():
  students = load_data()
  while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Students")
    print("2. Display Students")
    print("3. Search Students")
    print("4. Update Student Records")
    print("5. Delete Students")
    print("6. Calculate Average Marks")
    print("7. Save Records & Exit")
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
      add_student(students)
    elif choice == "2":
      display_students(students)
    elif choice == "3":
      search_student(students)
    elif choice == "4":
      update_student(students)
    elif choice == "5":
      delete_student(students)
    elif choice == "6":
      display_students(students)
    elif choice == "7":
      print("Exiting Student Management System...")
      break
    else:
      print("Invalid choice. Try again.")


if __name__ == "__main__":
  main()