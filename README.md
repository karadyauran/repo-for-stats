# Personal Finance Tracker

## Introduction
The Personal Finance Tracker is a console-based application aimed at helping users manage their personal finances, track expenses, and ensure budget discipline. It's built using Python and follows a clean architecture design.

## Features
- User registration and authentication
- Add, view, and manage expenses and income sources
- Set budget limits and alerts for overspending
- Simple command-line interface for smooth interaction

## Requirements
- Python 3.8+
- Dependencies listed in `package.json` with main ones being:
  - `python-dotenv`
  - `bcrypt`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/personal-finance-tracker.git
   ```
2. Navigate into the project directory:
   ```bash
   cd personal-finance-tracker
   ```
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Set up your environment variables by copying `.env.example` to `.env` and adding necessary configurations.
2. Run the application:
   ```bash
   python main.py
   ```
3. Follow the menu prompts to register, log in, and start tracking your expenses.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## Credits
Created with assistance from OpenAI API. Contributions are welcome to enhance functionality and user experience.

## Contributing
Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.
