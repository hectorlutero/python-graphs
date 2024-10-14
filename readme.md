# Data Visualization with Python

This project uses Python to create bar charts from CSV data using matplotlib and pandas libraries.

## Overview

The `main.py` script reads data from a CSV file, processes it, and generates a bar chart comparing multiple numeric columns across different data sets.

## Requirements

- Python 3.x
- pandas
- matplotlib

## Installation

To install the required libraries, run:

```bash
pip install pandas matplotlib
```

README.md

## Usage

Ensure your CSV file (named data.csv) is in the same directory as the script.
Run the script:

```bash
python3 main.py
```

The script will generate and display a bar chart.

## CSV File Format

The CSV file should have the following structure:

- First column: 'Set' (labels for x-axis)
- Subsequent columns: Numeric data to be plotted

## Features

- Dynamically reads all numeric columns from the CSV file
- Generates a grouped bar chart for easy comparison
- Automatically adjusts bar positions and widths based on the number of columns
- Includes a legend for easy identification of data series

## Customization

You can modify the following aspects of the chart in the `main.py` file:

- Figure size: Adjust the `figsize` parameter in `plt.figure()`
- Colors: Matplotlib automatically assigns colors, but you can specify them if needed
- Title and axis labels: Modify the `plt.title()`, `plt.xlabel()`, and `plt.ylabel()` calls

## Output

The script generates a bar chart and displays it on screen. To save the chart as an image file, add the following line before `plt.show()`:

plt.savefig('output_chart.png')

This will save the chart as 'output_chart.png' in the same directory as the script.
