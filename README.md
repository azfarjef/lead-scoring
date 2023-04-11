# DHL Express Lead Scoring Tool

This project is a 42KL anchor partner project with DHL to develop a prototype tool designed to support DHL Express' lead generation process. The tool was developed by a team of three using Python and its packages such as pandas and fuzzywuzzy for data manipulation and analysis, and Tkinter for the frontend design to create a simple user experience.

## Project Overview

DHL Express aspires to build a clean B2B database of 400,000 to 500,000 customers through various touchpoints (e.g. customer service, operations, etc.). As part of its operational enhancement, the company sought to develop a tool that could better assist in their B2B lead generation.

The tool is designed to conduct simple data pre-processing based on provided datasets, filter relevant/irrelevant data, build a structure for standardized data entry, and score and prioritize leads based on certain predetermined criteria. The tool also provides basic insights on the process of converting leads to customers.
## Features

- User-friendly interface built with Tkinter.
- Standardized database structure for efficient data entry.
- Data pre-processing to filter relevant/irrelevant data and eliminate duplicates.
- Data scoring to prioritize leads based on certain predetermined criteria.
- Customize the scoring criteria.
- Merge functionality to add new incoming databases in CSV format to the current database.
- Search functionality to view the searched company's details

## Getting Started

To get started with this project, you'll need to have Python and the required packages installed.

Clone the repository to your local machine.
```bash
    git clone https://github.com/azfarjef/lead-scoring.git
```
Install the required packages
```bash
    pip install -r requirements.txt.
```
Go to compile directory
```bash
    cd compile
```
Run the main program by running the command
```bash
    ./main.py.
```
## Usage

- Before running the program, customize the scoring criteria which includes industry, competitors, lead source, employee count, total potential revenue, contact information and physical channel.
- Open the `weighted_adjustment.xlsx` file in `compile/data/` directory. Customize the scoring criteria in the `scoring adjustment` sheet.
- Click `Browse` button in the main program. Select the database files to be used/merged. Example database files are available in `compile/data/` directory.
- Click `Generate` button to clean (removing duplicates / irrelevant data) and score the data.
- A file (default: `results.xlsx`) will be created to store the results. The database is now cleaned and sorted based on the lead score.
## Demo
![output2](https://user-images.githubusercontent.com/73651474/231232995-9168243f-be4d-4b4d-8d25-56a555d81f5a.gif)

## Authors

- [@1ssyazz](https://github.com/1ssyazz)
- [@seezhong](https://github.com/seezhong)
- [@azfarjef](https://github.com/azfarjef)
## Acknowledgements

We would like to thank DHL Express for the opportunity to develop this tool and our team members for their contributions to the project.
