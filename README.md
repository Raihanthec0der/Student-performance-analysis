# 🎓 Student Performance Analysis

An exploratory data analysis (EDA) project that investigates student academic performance and explores relationships between final grades and factors such as study time, previous failures, absences, gender, address type, and parental education.

## 📌 Project Overview

This project analyzes a dataset containing **395 students and 33 variables**.

The main academic outcome is **G3**, the final grade.

The analysis follows a practical data-analysis workflow:

**Load → Inspect → Validate → Analyze → Visualize → Interpret**

## 🎯 Objectives

- Understand the structure and quality of the dataset.
- Check for missing values and duplicate records.
- Analyze the distribution of final grades.
- Explore study time and previous failures in relation to final grades.
- Examine demographic and family-related factors.
- Measure the relationship between absences and final grades.
- Analyze correlations between G1, G2, and G3.
- Produce reusable, high-resolution visualizations.

## 🛠️ Technologies

- **Python 3.10+**
- **Pandas**
- **Matplotlib**

## 📁 Project Structure

```text
Student-Performance-Analysis/
│
├── data/
│   ├── student_data.csv
│   └── README.md
│
├── notebooks/
│   └── README.md
│
├── src/
│   └── main.py
│
├── visualizations/
│   └── generated charts
│
├── .gitignore
├── README.md
└── requirements.txt
```

## 📊 Dataset

This project uses a student performance dataset containing academic, demographic, family, and study-related information.

### Dataset Source

- **Platform:** Kaggle
- **Dataset:** Student Performance Data
- **Dataset Author:** Devansodariya
- **Source:** https://www.kaggle.com/datasets/devansodariya/student-performance-data

The dataset is used in this project for educational purposes, exploratory data analysis (EDA), statistical analysis, and data visualization.

The analysis expects:

```text
data/student_data.csv
```

The dataset used during analysis contains:

- **395 rows**
- **33 columns**
- **0 duplicate rows**
- **0 missing values**

Important variables include:

| Variable | Meaning |
|---|---|
| `G1` | First-period grade |
| `G2` | Second-period grade |
| `G3` | Final grade |
| `studytime` | Weekly study-time level |
| `failures` | Number of previous class failures |
| `absences` | Number of school absences |
| `Medu` | Mother's education level |
| `Fedu` | Father's education level |
| `sex` | Student gender |
| `address` | Urban/Rural address type |

## 🔍 Key Findings

### 1. G2 has the strongest relationship with G3

The correlation analysis produced:

```text
G1 ↔ G3 = 0.801
G2 ↔ G3 = 0.905
```

`G2` therefore showed the strongest positive linear relationship with final grade `G3` among the three grade variables.

> Correlation does not imply causation.

### 2. Previous failures are associated with lower final grades

Average G3 by previous failures:

| Previous Failures | Average G3 |
|---:|---:|
| 0 | 11.25 |
| 1 | 8.12 |
| 2 | 6.24 |
| 3 | 5.69 |

Students with more previous failures had substantially lower average final grades in this dataset.

### 3. Study time shows a generally positive pattern

| Study Time Level | Average G3 |
|---:|---:|
| 1 | 10.05 |
| 2 | 10.17 |
| 3 | 11.40 |
| 4 | 11.26 |

The relationship is not perfectly monotonic, but higher study-time levels generally corresponded to higher average final grades.

### 4. Absences had almost no linear correlation with G3

```text
Absence vs G3 correlation = 0.034
```

This indicates a very weak linear relationship between absences and final grades in this dataset.

### 5. Parental education shows a generally positive pattern

For education levels 1–4, both maternal and paternal education generally increased alongside average G3.

Small groups should be interpreted cautiously. For example, `Fedu = 0` contains only 2 students.

## 📈 Visualizations

The analysis generates:

- `failures_vs_g3.png`
- `studytime_vs_g3.png`
- `gender_vs_g3.png`
- `address_vs_g3.png`
- `mothers_education_vs_g3.png`
- `fathers_education_vs_g3.png`
- `grade_correlation.png`

Run the analysis to generate or refresh these files.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Raihanthec0der/Student-Performance-Analysis.git
cd Student-Performance-Analysis
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the dataset

Place your CSV here:

```text
data/student_data.csv
```

### 5. Run the analysis

From the project root:

```bash
python src/main.py
```

The script prints the analysis results and saves the charts inside:

```text
visualizations/
```

## 🧪 Data Quality Checks

The script automatically checks:

- Dataset shape
- Column names
- Duplicate rows
- Missing values
- Descriptive statistics
- Required columns

If the dataset is missing or required columns are absent, the script provides a clear error message instead of failing with an unclear file/path error.

## 💡 Skills Demonstrated

This project demonstrates practical skills in:

- Python
- Pandas
- Data inspection
- Data-quality validation
- GroupBy analysis
- Descriptive statistics
- Correlation analysis
- Data visualization
- File-path handling with `pathlib`
- Reusable Python functions
- GitHub project organization

## ⚠️ Interpretation Note

This is an exploratory analysis project. The observed relationships are associations within the dataset and should not automatically be interpreted as causal effects.

## 📜 License

This project is released under the MIT License. See `LICENSE`.

## 👤 Author

**MD. Abdullah Al Raihan**

Data Science learner focused on Python, Data Analysis, and practical projects.
