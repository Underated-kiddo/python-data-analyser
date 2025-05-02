import pandas as pd
import matplotlib.pyplot as plt  

# Initializing df 
df = None

try:
    df = pd.read_csv("todays_data.csv")  
    print("CSV file uploaded successfully")
except FileNotFoundError:
    print("The file in task isn't found. Check the spelling or upload the file.")
except Exception as e:
    print(f"Error loading CSV file: {e}")

# Proceed only if df is successfully loaded
if df is not None:
    print("The first 5 rows of data :")
    print(df.head())

    print("\n  Data info :")
    print(df.info())
    print("\n -Missing values :")
    print(df.isnull().sum())

    df.dropna(inplace=True)

    print(" data Statistics :")
    print(df.describe())

    # grouped by categorical column
    if 'species' in df.columns:
        print("\n  Grouped Means by academic level:")
        print(df.groupby('academic level').mean(numeric_only=True))

    print("\n This is a line graph")
    plt.figure()
    plt.plot(df.index, df[df.columns[0]]) 
    plt.title("Line Chart")
    plt.xlabel("Index")
    plt.ylabel(df.columns[0])
    plt.grid(True)
    plt.show()

    # Bar chart: Average Academic Level by Gender
    if 'Gender' in df.columns and 'Academic Level' in df.columns:
        print("\nThis is a bar chart")
        bar_data = df.groupby('Gender')['Academic Level'].count()
        plt.figure()
        plt.bar(bar_data.index, bar_data.values)
        plt.title("Bar Chart: Count of Academic Levels by Gender")
        plt.xlabel("Gender")
        plt.ylabel("Count")
        plt.show()
    else:
        print("Bar chart cannot be created. Ensure 'Gender' and 'Academic Level' columns exist in the data.")

    # Histogram: Distribution of Academic Levels
    if 'Academic Level' in df.columns:
        print("\nThis is a histogram")
        plt.figure()
        plt.hist(df['Academic Level'], bins=10, color='lightblue', edgecolor='black')
        plt.title("Histogram: Distribution of Academic Levels")
        plt.xlabel("Academic Level")
        plt.ylabel("Frequency")
        plt.show()
    else:
        print("Histogram cannot be created. Ensure 'Academic Level' column exists in the data.")

    # Scatter plot: Gender vs Academic Level
    if 'Gender' in df.columns and 'Academic Level' in df.columns:
        print("\nThis is a scatter plot")
        plt.figure()
        plt.scatter(df['Gender'], df['Academic Level'], alpha=0.7)
        plt.title("Scatter Plot: Gender vs Academic Level")
        plt.xlabel("Gender")
        plt.ylabel("Academic Level")
        plt.grid(True)
        plt.show()
    else:
        print("Scatter plot cannot be created. Ensure 'Gender' and 'Academic Level' columns exist in the data.")