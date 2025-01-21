# Personal Finance Manager

## Overview
The Personal Finance Manager is a console application designed to help individuals track their expenses and incomes, manage budgets, and set savings goals effectively.

## Features
- **Expense Tracking:** Log daily expenses with categories and optional tags.
- **Income Management:** Record various income sources.
- **Budget Setting:** Define monthly budgets for different categories and get alerts for budget breaches.
- **Savings Goals:** Set and track progress towards savings goals.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/personal_finance_manager.git
   ```
2. Navigate to the project directory:
   ```bash
   cd personal_finance_manager
   ```
3. Set up the virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt  # Create this file if necessary
   ```

## Usage
Run the application using the following command:
```bash
python -m personal_finance_manager/main.py
```

For available commands, refer to the help:
```bash
python -m personal_finance_manager/main.py --help
```

## Testing
To run tests:
```bash
python -m unittest discover -s personal_finance_manager/tests
```

## Contributions
Feel free to fork the repository and make contributions. Pull requests are welcome and will be reviewed promptly.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---

This project was created with the help of OpenAI API.