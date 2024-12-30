# Personal Finance Tracker

## Overview

The **Personal Finance Tracker** is a console-based application designed to help individuals keep track of their income, expenses, and balance their financial life. The project is implemented entirely in Python and follows a clean architecture design.

## Features
- User authentication
- Income and expense management
- Budget tracking and warnings
- Savings goal setting
- Financial reports

## Technology Stack
- **Python**: Core programming language used.
- **SQLite**: Optional for database storage (future expansion)

## Directory Structure
```plaintext
personal-finance-tracker/
│   package.json
│   .gitignore
│   README.md
│   .env.example
│   LICENSE
│
└───src/
    ├───models/
    │       finance.py
    ├───repositories/
    │       finance_repository.py
    ├───services/
    │       finance_service.py
    ├───controllers/
    │       finance_controller.py
    └───main.py
```

## Getting Started

### Prerequisites
Make sure you have Python 3.6 or later installed on your system.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/personal-finance-tracker.git
   cd personal-finance-tracker
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
To run the application, execute the following:
```bash
python src/main.py
```

## Contributing
This project was initially created by **OpenAI API**. Feel free to submit issues and enhancement requests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more detail.
