\# Expense Tracker CLI



A simple command-line expense tracker built with Python. It allows users to add, update, delete, list, and summarize their expenses using a JSON file for data storage.



\## Features



\* Add a new expense with a description and amount

\* Update an existing expense

\* Delete an expense by ID

\* View all expenses

\* View the total of all expenses

\* View expenses for a specific month of the current year

\* Validate negative or zero amounts

\* Validate invalid month values

\* Handle non-existent expense IDs

\* Store expense data in a JSON file



\## Technologies Used



\* Python 3

\* JSON

\* argparse

\* pathlib

\* datetime



\## Project Structure



```text

expense-tracker/

├── expense\_tracker.py

├── expenses.json

├── README.md

└── .gitignore

```



\## How to Run



Make sure Python is installed, then open a terminal in the project directory.



\### Add an Expense



```bash

python expense\_tracker.py add --description "Lunch" --amount 20

```



Example output:



```text

Expense added successfully (ID: 1)

```



\### List Expenses



```bash

python expense\_tracker.py list

```



\### Update an Expense



```bash

python expense\_tracker.py update --id 1 --description "Lunch at Restaurant" --amount 30

```



\### Delete an Expense



```bash

python expense\_tracker.py delete --id 1

```



\### View Total Expenses



```bash

python expense\_tracker.py summary

```



\### View Monthly Summary



```bash

python expense\_tracker.py summary --month 9

```



Example output:



```text

Total expenses for September: $30.00

```



\## Data Storage



Expenses are stored locally in `expenses.json`.



Each expense contains:



\* ID

\* Date

\* Description

\* Amount



Example:



```json

\[

&#x20;   {

&#x20;       "id": 1,

&#x20;       "date": "2026-09-24",

&#x20;       "description": "Lunch at Restaurant",

&#x20;       "amount": 30.0

&#x20;   }

]

```



\## Validation



The application handles common invalid inputs, including:



\* Negative or zero expense amounts

\* Invalid month numbers

\* Non-existent expense IDs



\## Project



This project was built as part of the roadmap.sh Expense Tracker project.



Roadmap: https://roadmap.sh/projects/expense-tracker



