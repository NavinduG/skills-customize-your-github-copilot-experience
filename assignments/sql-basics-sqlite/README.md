# 📘 Assignment: SQL Basics with SQLite

## 🎯 Objective

Learn database fundamentals by building a student management system. You will create database tables, write SQL queries to add and retrieve data, and connect Python to SQLite to persist information.

## 📝 Tasks

### 🛠️ Create the Database Schema

#### Description
Design and create a SQLite database with a `students` table to store student information.

#### Requirements
Completed program should:

- Create a SQLite database file named `students.db`
- Define a `students` table with columns: `id` (primary key), `name`, `email`, and `grade`
- Verify the table was created successfully by querying the database

### 🛠️ Insert and Query Student Records

#### Description
Write Python code to add student records to the database and retrieve them using SQL queries.

#### Requirements
Completed program should:

- Add at least 3 sample student records to the database
- Write a function to retrieve all students sorted by name
- Write a function to find a student by their email address
- Display query results in a readable format (e.g., a formatted table or list)

Example output:
```
All Students:
ID | Name          | Email                 | Grade
1  | Alice Johnson | alice@example.com     | A
2  | Bob Smith     | bob@example.com       | B
3  | Carol White   | carol@example.com     | A
```

### 🛠️ Update and Delete Records

#### Description
Implement functionality to modify and remove student records from the database.

#### Requirements
Completed program should:

- Write a function to update a student's grade by their id
- Write a function to delete a student record by their id
- Demonstrate both operations by updating and deleting a sample record
- Ensure data changes are persisted to the database (commit transactions)