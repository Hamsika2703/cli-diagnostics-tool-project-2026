Packaged CLI Diagnostics Tool

Overview

This project is a simple Python command-line tool that helps check basic system information. It collects details about the computer and checks whether important developer tools like Python and Git are available. It also creates reports in JSON and text formats so the results are easy to read and use.

Features

- Shows the operating system and Python version.
- Displays the machine architecture.
- Checks total and available disk space.
- Shows the current working directory and Python executable path.
- Counts environment variables without displaying their values.
- Checks whether Python and Git are available.
- Saves the results in JSON and text files.
- Handles operating system errors.
- Includes tests to check that the tool works as expected.

Requirements

- Python 3.10 or later
- pip
- pytest for running tests

Installation

Open the project folder in your terminal and run:

python -m pip install -e .

This installs the project in editable mode, which is useful while developing and making changes.

How to Run

Run the tool with this command:

python -m diagnostics_tool.cli

After running it, the tool displays the diagnostics in the terminal and creates two files:

- "diagnostics_report.json" – stores the results in JSON format.
- "diagnostics_report.txt" – stores the results in a simple text format.

Running Tests

To run the tests, use:

python -m pytest -v

The tests check whether the tool runs correctly, creates both reports, includes the expected system information, and handles missing developer tools and operating system errors.

Project Structure

cli-diagnostics-tools/
├── diagnostics_tool/
│   ├── __init__.py
│   └── cli.py
├── tests/
│   └── test_cli.py
├── pyproject.toml
└── README.md

The report files are created when the tool runs, so they may also appear in the project folder.

What I Learned

While working on this project, I learned how to collect system information using Python, create JSON and text reports, package a Python project, and write automated tests using pytest. I also learned how to handle errors and check whether developer tools are available.