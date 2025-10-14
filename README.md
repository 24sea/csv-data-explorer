# 🧩 CSV Data Explorer (with Flexible Imputation & Filtering)

### 📄 Overview

**CSV Data Explorer** is a **Python Command-Line Tool (CLI)** built for quick **data exploration and cleaning**.
It helps users understand and preprocess CSV datasets directly from the terminal — no need to open Excel or Jupyter.

This utility automates common **data preparation** steps like handling missing values, filtering rows, selecting columns, and exporting cleaned data.
It’s a reusable **data preprocessing component** for AI & ML pipelines.

---

### 🚀 Features

| Feature                       | Description                                                                        |
| ----------------------------- | ---------------------------------------------------------------------------------- |
| 🔍 **Data Summary**           | Displays dataset shape, column types, missing value count, and numeric statistics. |
| 🧹 **Imputation**             | Handles missing data automatically using mean or median values (`--impute`).       |
| 🧾 **Flexible Cleaning**      | Drop unnecessary columns like *Cabin* or filter only what you need.                |
| 🎯 **Row Filtering**          | Use `--query` to filter rows with conditions (e.g., `"Fare > 50 and Age < 40"`).   |
| 📊 **Column Selection**       | Use `--columns` to select specific columns to view or clean.                       |
| 💾 **Export Clean Data**      | Save the cleaned CSV with `--save-clean`.                                          |
| ⚙️ **Command-Line Interface** | Fully terminal-driven — no GUI required.                                           |

---

### 🧠 Why This Project

This tool demonstrates **data engineering and preprocessing**, which is the foundation of every AI/ML project.
It reflects real-world tasks that AI Engineers perform daily:

* Cleaning raw data before model training
* Handling missing and invalid values
* Selecting and filtering meaningful data
* Automating data wrangling via scripts

---

### 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** `pandas`, `numpy`, `argparse`, `pathlib`
* **Category:** Data Engineering / AI Data Preparation

---

### 🧩 How It Works

1️⃣ **Command-line input** is parsed using `argparse`.
2️⃣ The tool reads the CSV file using `pandas`.
3️⃣ Based on user-provided flags:

* Columns are selected
* Filters are applied (`--query`)
* Missing values are imputed (`--impute`)
* Columns may be dropped (`--drop-cabin`)
  4️⃣ A summary is printed, and cleaned data is saved if requested.

---

### 🧰 Example Commands

#### 1️⃣ Summarize a dataset

```bash
python src/explorer.py summary datasets/titanic.csv
```

#### 2️⃣ Summarize only specific columns

```bash
python src/explorer.py summary datasets/titanic.csv --columns Age,Fare,Survived
```

#### 3️⃣ Filter rows before summarizing

```bash
python src/explorer.py summary datasets/titanic.csv --query "Fare > 50 and Age < 40"
```

#### 4️⃣ Clean and impute missing data

```bash
python src/explorer.py clean datasets/titanic.csv --impute Age:median --impute Fare:mean
```

#### 5️⃣ Clean and save output

```bash
python src/explorer.py clean datasets/titanic.csv --impute Age:median --drop-cabin yes --save-clean datasets/titanic_clean.csv
```

---

### 📦 Installation

1️⃣ Clone this repository:

```bash
git clone https://github.com/24sea/csv-data-explorer
```

2️⃣ Navigate to project folder:

```bash
cd csv-data-explorer
```

3️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

---

### 📁 Project Structure

```
csv-data-explorer/
│
├── src/
│   └── explorer.py          # Main CLI script
│
├── datasets/
│   └── titanic.csv          # Example dataset
│
├── requirements.txt         # Required Python libraries
└── README.md                # Project documentation
```

---

### 🧩 Example Output

```
====== Original Summary ======
Shape: (418, 2)

Dtypes:
 Age     float64
Fare    float64

Missing values per column:
 Age     86
Fare     1

Numeric describe:
       count       mean        std   min      25%      50%   75%       max
Age   332.0  30.272590  14.181209  0.17  21.0000  27.0000  39.0   76.0000
Fare  417.0  35.627188  55.907576  0.00   7.8958  14.4542  31.5  512.3292
==============================
```

---

### 📚 Learning Highlights

✅ Command-line programming using **argparse**
✅ Modular code design with **functions**
✅ Data cleaning using **pandas**
✅ Error handling and reusability
✅ A real example of **data preprocessing** used in AI Engineering

---

### 🌟 Future Enhancements (AI-Focused)

* `--scale` → Normalize numeric columns
* `--encode` → Encode categorical features
* `--split` → Train/Test data splitting
* `--report` → Generate Markdown summary report
* `--chunksize` → Handle large CSV files in parts

---

### 👩‍💻 Author

**Sonal Sharma**
*Aspiring AI Engineer | Python Developer | Data Enthusiast*

