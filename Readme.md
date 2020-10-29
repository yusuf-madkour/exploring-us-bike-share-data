# Exploring US bike share data

## Description

This project is part of the [Udacity data analysis nanodegree](confirm.udacity.com/HESYY4DD).

In this project, I am exploring data related to bike share systems for three major cities in the United States; Chicago, New York City, and Washington. After taking input from the user, this script answers interesting questions about the data by computing descriptive statistics using [pandas library](https://pandas.pydata.org/pandas-docs/stable/index.html).

![demo gif](https://github.com/yusuf-madkour/exploring-us-bike-share-data/blob/master/demo.gif)

## Requirements

Language: Python 3.7 or above

Supported OS: Linux

Use one of the following commands in terminal after navigating to the project's directory to install the project requirements.

```bash
conda env create -f environment.yml
```

or

```bash
pip install -r requirements.txt
```

## Usage

Run the commands below from terminal after navigating to the project directory.

```bash
conda activate bikeshare
python bikeshare.py
```

## Script Flow

### User Input

The script uses [bullet library](https://github.com/bchao1/bullet) to take input from the user. The user must choose one of the three aforementioned cities. Afterwards, the user is asked to choose the filters based on which the statistics are computed.

**Available filters:**

- Month: filter by a specific month only
- Day: filter by a specific day of the week only
- Both: filter by a specific month and day of the week
- None: no filters

The user is then prompted to choose the month, day or both based on the filter choice.

### Presenting Statistics

**Station statistics:**

1. Most used start station
2. Most used end station
3. Most used combination of start and end stations

**Trip duration statistics:**

1. Total trip duration
2. Average trip duration

**User statistics:**

1. Subscribers vs. customers distribution
2. Gender distribution
3. Earliest year of birth, most recent year of birth and most common year of birth

### Displaying raw data

The user is prompted if he/she wishes to view individual raw trip data. If the user inputs "yes", the data of 5 trips will be presented in raw format.

The same prompt is repeated until the user inputs "no". The user is finally prompted if he/she wishes to restart the exploration.

## TODO

- Add visualizations using plotly or termplotlib
