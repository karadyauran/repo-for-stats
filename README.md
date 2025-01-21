# Task Manager Console App

## Overview
The Task Manager Console App is a simple command-line interface application designed to help users manage their tasks effectively. Users can add, update, delete, and list tasks directly from their console. This project follows clean architecture principles and was created with the help of OpenAI API.

## Features
- Add new tasks with titles, descriptions, and due dates.
- Update task details or mark them as completed or pending.
- Delete existing tasks.
- List all tasks with filtering options.

## Installation

1. **Clone the repository:**
   ```shell
   git clone https://github.com/yourusername/task-manager-console-app.git
   cd task-manager-console-app
   ```

2. **Ensure you have Python 3.9 or newer:**
   The application requires Python 3.9 or higher to run.

3. **Set up a virtual environment:**
   ```shell
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install dependencies:**
   There are no external dependencies needed for this project.

## Usage

Start the application by running:
```shell
python main.py
```
Follow the on-screen commands to manage your tasks.

## Project Structure
- **entities/**: Contains the `Task` entity class.
- **usecases/**: Hosts the `TaskManager` class that encapsulates the core business logic.
- **interfaces/**: Defines interfaces such as `TaskRepository` and `OutputBoundary` for dependency inversion.
- **repositories/**: Implements storage logic with `TaskFileRepository` and `TaskMemoryRepository`.
- **controllers/**: Contains the `TaskController` class that handles requests from the console.

## License
This project is licensed under the MIT License.

## Author
Created by [Your Name]. Contributions are welcome! Please submit pull requests and issues on GitHub. 

---
This project was generated using the OpenAI API, emphasizing clean and maintainable code.