# src/explorer.py
import sys
import argparse
import pandas as pd
import numpy as np
from pathlib import Path

def print_summary(df, title="Summary"):
    print("\n" + "="*6, title, "="*6)
    print("Shape:", df.shape)
    print("\nDtypes:\n", df.dtypes)
    print("\nMissing values per column:\n", df.isnull().sum())
    # numeric only describe for clarity
    print("\nNumeric describe:\n", df.select_dtypes(include=[np.number]).describe().T)
    print("="*30 + "\n")

def load_csv(path):
    return pd.read_csv(path)

def impute_column(df, col, method):
    """Impute a numeric column with 'median' or 'mean' or 'none'."""
    if method is None or method.lower() == 'none':
        return df, 0
    if col not in df.columns:
        return df, 0
    if method.lower() not in ('median','mean'):
        raise ValueError("impute method must be 'median', 'mean' or 'none'")
    before_na = df[col].isna().sum()
    if method.lower() == 'median':
        fill = df[col].median()
    else:
        fill = df[col].mean()
    df[col] = df[col].fillna(fill)
    coerced = before_na - df[col].isna().sum()  # number filled
    return df, int(coerced)

def parse_args(argv):
    p = argparse.ArgumentParser(prog="explorer.py", description="CSV Data Explorer - simple")
    p.add_argument('command', choices=['summary','clean'], help='command to run')
    p.add_argument('path', help='path to csv file')
    p.add_argument('--impute-age', choices=['median','mean','none'], default='median', help='how to impute Age')
    p.add_argument('--impute-fare', choices=['median','mean','none'], default='median', help='how to impute Fare')
    p.add_argument('--drop-cabin', choices=['yes','no'], default='yes', help='drop Cabin column?')
    p.add_argument('--save-clean', default=None, help='optional path to save cleaned csv (e.g., cleaned.csv)')
    p.add_argument('--columns', help='comma-separated list of columns to keep (optional)')
    p.add_argument('--query', help='(filters if any condition given by user)')
    p.add_argument('--impute',action='append',metavar='COL:METHOD',help="Repeatable. Example: --impute Age:median --impute Fare:mean")
    return p.parse_args(argv[1:])

def run_summary(path, columns, query):
    df = load_csv(path)

    # ✅ Apply column selection (if user gave --columns)
    if columns:
        selected_cols = [c.strip() for c in columns.split(",") if c.strip() in df.columns]
        missing_cols = [c.strip() for c in columns.split(",") if c.strip() not in df.columns]

        if missing_cols:
            print(f"Ignored missing columns: {', '.join(missing_cols)}")

        df = df[selected_cols]

    if query:
        df=df.query(query)

    # ✅ Now print summary
    print_summary(df, "Original Summary")



def run_clean(path, impute_age, impute_fare, drop_cabin, save_clean_path, columns, query, impute):
    df = load_csv(path)
    # ✅ Apply column selection (if user gave --columns)
    if columns:
        selected_cols = [c.strip() for c in columns.split(",") if c.strip() in df.columns]
        missing_cols = [c.strip() for c in columns.split(",") if c.strip() not in df.columns]

        if missing_cols:
            print(f"Ignored missing columns: {', '.join(missing_cols)}")

        df = df[selected_cols]

    if query:
        df= df.query(query)
    print_summary(df, "Original Summary")
    
    # ✅ Apply flexible imputation rules
    if impute:
        total_coerced = {}
        for rule in impute:
            try: 
                col, method = rule.split(":", 1)
                col, method = col.strip(), method.strip().lower()

                if col not in df.columns:
                     print(f"Column '{col}' not found — skipped.") 
                     continue
                if method not in ("mean", "median", "none"): 
                    print(f"Invalid method '{method}' for {col} — skipped.") 
                    continue
                if not pd.api.types.is_numeric_dtype(df[col]): 
                    print(f"Column '{col}' is not numeric — skipped.")
                    continue
                df, filled = impute_column(df, col, method)
                total_coerced[col] = filled
            except ValueError: 
                print(f"Invalid format for rule '{rule}'. Use COL:METHOD.") 
            print("Imputation counts:", total_coerced)
    total_coerced = {}
    # Impute Age
    df, coerced_age = impute_column(df, 'Age', impute_age)
    total_coerced['Age'] = coerced_age

    # Impute Fare
    df, coerced_fare = impute_column(df, 'Fare', impute_fare)
    total_coerced['Fare'] = coerced_fare

    # Drop Cabin if requested
    if drop_cabin == 'yes' and 'Cabin' in df.columns:
        df = df.drop(columns=['Cabin'])

    print_summary(df, "Cleaned Summary")
    print("Imputation counts (how many values filled):", total_coerced)

    if save_clean_path:
        out = Path(save_clean_path)
        df.to_csv(out, index=False)
        print(f"Saved cleaned CSV to: {out}")

def main(argv):
    args = parse_args(argv)
    path = args.path
    if not Path(path).exists():
        print("CSV file not found:", path)
        return

    if args.command == 'summary':
        run_summary(path, args.columns, args.query)
    elif args.command == 'clean':
       run_clean(
    path,
    args.impute_age,
    args.impute_fare,
    args.drop_cabin,
    args.save_clean,
    args.columns,
    args.query,
    args.impute)
    else:
        print("Unknown command")

if __name__ == "__main__":
    main(sys.argv)
