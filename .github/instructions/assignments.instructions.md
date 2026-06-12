---
description: "Instructions to use whenever creating or editing assignment markdown files to ensure consistency and clarity for students."
applyTo: "assignments/**/*.md"
---

# Assignment Markdown Structure Guidelines

All assignment markdown files should follow these guidelines:

## 1. Template Usage

- Assignment markdown files must follow the structure in [`templates/assignment-template.md`](../../templates/assignment-template.md).
- Each assignment should live in its own folder and use a `README.md` file as the main entry point.
- Do not remove, rename, or skip required sections from the template.

## 2. Section Guidance

Use the template headings exactly, including the icon usage and section order:

- `# 📘 Assignment: [Assignment Title]`
- `## 🎯 Objective`
- `## 📝 Tasks`
- `### 🛠️ [Task Title]`
- `#### Description`
- `#### Requirements`

- **Title**: Replace `[Assignment Title]` with a short, descriptive name such as `Python Basics` or `Functions and Modules`.
- **Objective**: Write 1-2 student-friendly sentences that explain what the assignment teaches or accomplishes.
- **Tasks**: For each task, use a specific action-oriented title, write a clear description of what the student must do, and list measurable requirements with bullets.
- Include example input/output in code blocks only when it helps students complete the work.

## 3. Style Standards

- Keep the language clear, encouraging, and focused on learning goals.
- Use consistent markdown formatting across assignments.
- Do not include extra sections unless explicitly specified in the assignment.