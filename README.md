# Python Data Analysis and Visualization

This project demonstrates how to load, analyze, and visualize data using Python. The script performs basic data exploration, analysis, and creates various types of visualizations using the `pandas` and `matplotlib` libraries.

## Features

1. **Data Loading and Exploration**
   - Loads a dataset from a CSV file.
   - Displays the first few rows of the dataset.
   - Provides information about the dataset structure, including data types and missing values.
   - Cleans the dataset by dropping rows with missing values.

2. **Basic Data Analysis**
   - Computes basic statistics (mean, median, standard deviation, etc.) for numerical columns.
   - Groups data by a categorical column and computes the mean of numerical columns for each group (if applicable).

3. **Data Visualization**
   - **Line Chart**: Visualizes trends over the dataset index.
   - **Bar Chart**: Compares the count of a numerical value across categories (e.g., Academic Levels by Gender).
   - **Histogram**: Shows the distribution of a numerical column.
   - **Scatter Plot**: Visualizes the relationship between two numerical columns (e.g., Gender vs. Academic Level).

## Requirements

- Python 3.x
- pandas
- matplotlib

## How to Run

1. Ensure you have Python installed on your system.
2. Install the required libraries using pip:
   ```bash
   pip install pandas matplotlib
   ```
3. Place the CSV file (`todays_data.csv`) in the same directory as the script.
4. Run the script:
   ```bash
   python py analyser.py
   ```

## File Structure

```
Pyreader/
│
├──  analyser.py       # Python script for data analysis and visualization
├── todays_data.csv      # Dataset file (CSV format)
├── README.md            # Project documentation
```

## Notes

- Ensure the dataset contains the required columns (e.g., `Gender`, `Academic Level`, etc.) for all visualizations to work.
- If the dataset structure changes, you may need to update the script accordingly.

## Example Output

- **Line Chart**: Displays trends in the first column of the dataset.
- **Bar Chart**: Shows the count of Academic Levels by Gender.
- **Histogram**: Visualizes the distribution of Academic Levels.
- **Scatter Plot**: Plots the relationship between Gender and Academic Level.

## License

This project is for educational purposes and is not licensed for commercial use.