import sqlite3

DATABASE = "students.db"


def create_database():
    """Create the students database and table."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            grade TEXT
        )
        """
    )
    conn.commit()
    conn.close()
    print("Database and table created successfully.")


def add_student(name, email, grade):
    """Add a new student to the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO students (name, email, grade) VALUES (?, ?, ?)",
            (name, email, grade),
        )
        conn.commit()
        print(f"Added student: {name}")
    except sqlite3.IntegrityError:
        print(f"Error: Email {email} already exists.")
    finally:
        conn.close()


def get_all_students():
    """Retrieve all students sorted by name."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, email, grade FROM students ORDER BY name")
    students = cursor.fetchall()
    conn.close()

    return students


def find_student_by_email(email):
    """Find a student by email address."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, email, grade FROM students WHERE email = ?", (email,))
    student = cursor.fetchone()
    conn.close()

    return student


def update_student_grade(student_id, new_grade):
    """Update a student's grade by id."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("UPDATE students SET grade = ? WHERE id = ?", (new_grade, student_id))
    conn.commit()
    conn.close()
    print(f"Updated student {student_id} to grade {new_grade}")


def delete_student(student_id):
    """Delete a student record by id."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    print(f"Deleted student {student_id}")


def display_students(students):
    """Display students in a formatted table."""
    if not students:
        print("No students found.")
        return

    print("\n" + "=" * 60)
    print(f"{'ID':<5} {'Name':<20} {'Email':<25} {'Grade':<5}")
    print("=" * 60)
    for student in students:
        print(f"{student[0]:<5} {student[1]:<20} {student[2]:<25} {student[3]:<5}")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    # Create database
    create_database()

    # Add sample students
    add_student("Alice Johnson", "alice@example.com", "A")
    add_student("Bob Smith", "bob@example.com", "B")
    add_student("Carol White", "carol@example.com", "A")

    # Display all students
    print("\nAll students:")
    all_students = get_all_students()
    display_students(all_students)

    # Find a student by email
    print("Finding student by email (bob@example.com):")
    student = find_student_by_email("bob@example.com")
    if student:
        print(f"Found: {student}")
    else:
        print("Student not found.")

    # Update a student's grade
    update_student_grade(1, "A+")

    # Delete a student
    delete_student(3)

    # Display updated list
    print("\nFinal student list:")
    final_students = get_all_students()
    display_students(final_students)