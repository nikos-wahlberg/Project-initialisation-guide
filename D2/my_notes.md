# 🐼 Pandas Essential Functions Cheat Sheet

### Phase 1: Ingestion & Exploration
* **`pd.read_csv()`** : Loads data from a CSV file into a DataFrame.
* **`df.head(n)`** : Displays the first n rows (default is 5).
* **`df.info()`** : Shows column names, data types, and missing value counts.
* **`df.describe()`** : Generates summary statistics for numerical columns.
* **`df.shape`** : Returns the number of rows and columns as a tuple.

### Phase 2: Selection & Filtering
* **`df['column']`** : Selects a single specific column.
* **`df.loc[]`** : Accesses rows/columns by label (names).
* **`df.iloc[]`** : Accesses rows/columns by integer index (position).
* **`df.query()`** : Filters data using a text-based expression.
* **`df.sort_values()`** : Reorders rows based on specific column values.

### Phase 3: Cleaning & Preparation
* **`df.isnull().sum()`** : Counts missing values per column.
* **`df.dropna()`** : Removes any rows or columns containing null values.
* **`df.fillna(val)`** : Replaces missing values with a specific number/text.
* **`df.drop_duplicates()`** : Removes identical rows from the dataset.
* **`df.rename()`** : Changes column names or index labels.
* **`df.astype()`** : Converts a column to a different data type.

### Phase 4: Transformation & Analysis
* **`df.groupby()`** : Groups data for calculations (e.g., sums by category).
* **`df.agg()`** : Runs multiple calculations (mean, max, etc.) at once.
* **`df.merge()`** : Combines two DataFrames using a shared key (SQL Join).
* **`df.apply()`** : Runs a custom Python function on every row or column.
* **`df.pivot_table()`** : Summarizes data into a spreadsheet-style grid.

### Phase 5: Exporting Results
* **`df.to_csv()`** : Saves the DataFrame to a CSV file.
* **`df.to_excel()`** : Saves the DataFrame to an Excel file.
* **`df.to_json()`** : Converts data to JSON format for web APIs.