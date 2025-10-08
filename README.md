# CSV Data Explorer (with Big File Support)

A command-line tool built with **Python, Pandas, and NumPy** to explore and clean large CSV files efficiently.

## 🚀 Features
- Summarizes CSV files: shape, data types, missing values
- Cleans data: fills missing numeric values (mean/median)
- Drops unnecessary columns (like Cabin)
- Optionally saves the cleaned file

## 💻 Usage
```bash
python src/explorer.py summary datasets/titanic.csv
python src/explorer.py clean datasets/titanic.csv --drop-cabin yes --save-clean datasets/titanic_clean.csv
