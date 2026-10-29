# Student Management System – DevOps Project

## 1. Project Overview
This project implements a Student Management System using Python and applies DevOps practices to automate testing and prepare the application for deployment.

## 2. Features
- Add student records
- View student records
- Search students by ID
- Delete student records
- Validate student information

## 3. Technologies Used
- Python
- pytest
- Git and GitHub
- GitHub Actions
- Docker
- Visual Studio Code

## 4. Automated Testing
The application includes six automated test cases to verify student creation, retrieval, deletion, invalid marks, duplicate student IDs, and empty student names.

Run the tests using:

```bash
python -m pytest -v
```

## 5. Continuous Integration
GitHub Actions is configured to run automated tests whenever code is pushed to the main branch or a pull request targets the main branch.

## 6. Docker
Build the application image:

```bash
docker build -t student-management .
```

Run the application:

```bash
docker run -it --rm student-management
```

## 7. Test Results
All six automated test cases passed during local testing.

## 8. Conclusion
This project demonstrates DevOps practices through version control, automated testing, continuous integration, and Docker containerization.
