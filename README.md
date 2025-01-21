# Personal Finance Manager

## Overview
The Personal Finance Manager is a console application designed to help users effectively manage their personal finances. This tool allows users to track their expenses and manage their budget efficiently.

## Features
1. **User Authentication**: Secure user account creation and login system.
2. **Expense Tracking**: Log daily expenses with categories and amounts.
3. **Budgeting**: Set budget limits for specific categories.
4. **Reports**: Generate reports to summarize spending and budget adherence.
5. **Data Export**: Export financial data to CSV for further analysis.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/personal-finance-manager.git
   cd personal-finance-manager
   ```

2. **Setup the environment**:
   Create a virtual environment and install dependencies (if there are any):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Environment Variables**:
   Define environment variables in the `.env` file by copying `.env.example`.
   ```bash
   cp .env.example .env
   ```
   Modify the necessary configuration details in `.env`.

## Usage
Run the application using the command line:
```bash
python3 src/main.py
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
This application was created using the OpenAI API.